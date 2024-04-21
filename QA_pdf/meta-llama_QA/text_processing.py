import torch
from transformers import StoppingCriteria, StoppingCriteriaList
import transformers

class StopOnTokens(StoppingCriteria):
    def __init__(self, stop_token_ids):
        self.stop_token_ids = stop_token_ids

    def __call__(self, input_ids: torch.LongTensor, **kwargs) -> bool:
        for stop_ids in self.stop_token_ids:
            if torch.eq(input_ids[0][-len(stop_ids):], stop_ids).all():
                return True
        return False


def initialize_stopping_criteria(stop_token_ids):
    stopping_criteria = StoppingCriteriaList([StopOnTokens(stop_token_ids)])
    return stopping_criteria


def initialize_generate_text_pipeline(model, tokenizer, stopping_criteria):
    generate_text = transformers.pipeline(
        model=model,
        tokenizer=tokenizer,
        return_full_text=True,
        task='text-generation',
        stopping_criteria=stopping_criteria,
        temperature=0.1,
        max_new_tokens=512,
        repetition_penalty=1.1
    )
    return generate_text


def initialize_stop_token_ids(stop_list, tokenizer, device):
    stop_token_ids = [tokenizer(x)['input_ids'] for x in stop_list]
    stop_token_ids = [torch.LongTensor(x).to(device) for x in stop_token_ids]
    return stop_token_ids
