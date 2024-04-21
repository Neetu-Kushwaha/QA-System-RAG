from torch import cuda, bfloat16
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


def initialize_model(model_id, hf_auth):
    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=bfloat16
    )
    model_config = AutoConfig.from_pretrained(
        model_id,
        use_auth_token=hf_auth
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        config=model_config,
        quantization_config=bnb_config,
        device_map='auto',
        use_auth_token=hf_auth
    )
    model.eval()
    print(f"Model loaded on {device}")
    return model


def initialize_tokenizer(model_id, hf_auth):
    return AutoTokenizer.from_pretrained(
        model_id,
        use_auth_token=hf_auth
    )
