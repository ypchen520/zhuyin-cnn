from transformers import AutoModelForImageClassification, TrainingArguments, Trainer, AutoTokenizer
from datasets import load_dataset

## dataset

dataset = load_dataset("yelp_review_full")
# dataset.save_to_disk("../dataset-toy/")
print(dataset["train"][100])

### Tokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True) # padding? truncation? TODO

tokenized_datasets = dataset.map(tokenize_function, batched=True) # batched? TODO

### Smaller subset

smaller_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
smaller_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))

## Train



# VIT?

# Trainer?