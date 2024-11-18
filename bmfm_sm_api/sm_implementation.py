# Run in conda environment bmfm-sm
#
# First-pass proof of concept based on BMFM code with a minimum of changes.
# This is also a first time D Elzinga (DE) uses the Open-AD model-onboarding
# template by B Duenas (BD). It serves to harden and improve the model-onboarding
# template as well as a first draft of onboarding BMFM OptiMol models, part
# of BmfmSM (small molecule) models.

# DE recommends installing bmfm-sm parallel to bmfm-examples and
# bmfm-service in a bmfm parent directory; eg, "bmfm".
#
# Given current BMFM-repos hard-coded assumptions about relative paths on disk,
# DE suggests also editable (pip-)install of bmfm-service, bmfm-sm repos:
#
# pip install -e path/to/bmfm-service  # parallel to bmfm-sm installation
# pip install -e path/to/bmfm-sm
import os
import traceback
from openad_service_utils import SimplePredictor, PredictorTypes, DomainSubmodule
from pydantic.v1 import Field
from dataclasses import asdict

from bmfm_sm.api.smmv_pretrained_model import SmallMoleculeMultiViewPretrainedModel

# from bmfm_sm.api.bmfm_pretrained_model import BMFMPretrainedModel
from bmfm_sm.api.dataset_registry import DatasetRegistry
from bmfm_sm.core.data_modules.namespace import Modality

# from models_main.bmfmsm_utils import get_predictions_text
from bmfm_sm.api.smmv_api import SmallMoleculeMultiViewModel

from docs.builder import doc_generate


class BmfmSM_Predictor(SimplePredictor):
    # Step 1. S3 parameters are the first to set up:
    property_type = PredictorTypes.MOLECULE  # BmfmSM properties are for small molecules
    # Path elements in path hierarchy order:
    domain = DomainSubmodule("molecules")  # Properties require `domain` to be set, becomes part of the path.
    algorithm_name = "small_molecules"
    algorithm_application = "full_sm"
    algorithm_version = "v0"
    # algorithm_version = "v0/bmfm_model_dir/finetuned/text/text_80M3E_rscfld/TOX21"
    # list of available property models in class
    available_properties = doc_generate()

    # Step 2 would be to set up API params.

    # Step 3 implement the setup_model function:
    def setup(self):
        # Plug in all the code where it does Dataset stuff, does the predictor
        # how it would run, and just do it for 1 concrete model.
        os.environ["BMFM_HOME"] = self.get_model_location()
        print(self.get_model_location())
        # Right now samples is actually singular, the molecule, eg, "C1Nc2ccccc2C1(OC1(CC)C(OO1))"

    def predict(self, samples):
        # This function is returned by setup_model.
        # `samples` is SMILES strings.
        # Copy the code where it invokes the model.forward() for inference
        # end_index = self.get_model_location().find('v0') + len('v0')  # moving home dir backwards due to sm
        # os.environ["BMFM_HOME"] = self.get_model_location()[:end_index]
        model = self.get_selected_property()
        print(f"sample: {samples},  selected model: {model}")
        result = {samples: {}}
        model_dataset = DatasetRegistry.get_instance().get_dataset_info(model)
        d_model = SmallMoleculeMultiViewModel.from_finetuned(model_dataset)
        d_model.eval()
        try:
            # model_result = get_predictions_text(samples, model_dataset, text_finetuned_checkpoint=d_model).tolist()
            model_result = SmallMoleculeMultiViewModel.get_predictions(
                samples, model_dataset, finetuned_model=d_model
            ).tolist()
            result = model_result
            # result[samples][model] = model_result
        except Exception as e:
            print("Error in model", model)
            print(f"Exception: {str(e)}")
            traceback.print_exc()
            raise e
            # result[samples][model] = "model failed to run"
        return result  # previously also returned `descriptions`


# register the model
BmfmSM_Predictor.register()

if __name__ == "__main__":
    from openad_service_utils import start_server

    # start server that picks up registered sm model
    start_server(max_workers=10)
