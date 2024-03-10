### All changes include
Koziev is the unsung hero here: https://github.com/state-spaces/mamba/pull/83
- Make MambaConfig class available from outside in order to allow MambaLMHeadModel customization via constructor config argument. mamba/mamba_ssm
/models/model__init__.py is changed
- Add json to Mamba config and add filter to config keys in from_pretrained so config.json can have fields _name_or_path and architectures like other models on hf.  
mamba/mamba_ssm/models/mixer_seq_simple.py and mamba/mamba_ssm/models/config_mamba.py is changed.
- Make MambaLMHeadModel input labels and return loss as a first element from forward like HuggingFace Transformer. mamba/mamba_ssm/models/mixer_seq_simple.py is changed.
Remember these 3 files so that whenever these 3 classes are imported to another file, we need to change import lines to refer to these 3 files.

Also we need to refer to local mamba_ssm instead of installed mamba. This way we can still inherit pre-built wheel from based mamba package - really important because it includes nvcc which you can't run at all without it. This follows normal instruction as exactly as based mamba: https://github.com/state-spaces/mamba
