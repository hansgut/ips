from transformers import AutoTokenizer, AutoConfig
import os

tokenizer = AutoTokenizer.from_pretrained('Salesforce/xgen-7b-8k-base')
config = AutoConfig.from_pretrained('Salesforce/xgen-7b-8k-base')

tokenizer.save_pretrained('./my_tokenizer')
config.save_pretrained('./my_tokenizer_config')

tokenizer = AutoTokenizer.from_pretrained('./my_tokenizer')