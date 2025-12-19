from ty3.core.env import Envars
from ty3.core.fs import *


TYEFI_ROOT = path(os.environ["TYEFI_ROOT"])
cfg = Envars(TYEFI_ROOT["tyefi.env"].absolute)
RUNTIME_DIR = path(cfg.get("DSP_RUNTIME_DIR", TYEFI_ROOT["/bin/dsp"]))
FILE_STORE_ROOT = path(cfg.get("DSP_FILE_STORE_ROOT", f"{TYEFI_ROOT}/bin/dsp"))
DSP_PROFILES_DIR = path(cfg.get("DSP_PROFILES_DIR", TYEFI_ROOT["dsp/profiles"]))
DSP_SETTINGS_FILE = TYEFI_ROOT["dsp/dspsettings.json"] # "/usr/share/hifiberry/dspprofiles"
