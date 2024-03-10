__version__ = "1.2.0.post1"

# refer to local mamba_ssm instead of based mamba_ssm.
import sys
#sys.path.insert(0, '/path/to/local/mamba-ssm') to import mamba-ssm from local directory
sys.path.insert(0, '/mnt/fast/nobackup/users/nt00601/mamba-finetune/mamba_ssm')
import mamba_ssm

from mamba_ssm.ops.selective_scan_interface import selective_scan_fn, mamba_inner_fn
from mamba_ssm.modules.mamba_simple import Mamba
from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel
from mamba_ssm.models.config_mamba import MambaConfig

