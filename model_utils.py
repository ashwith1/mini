from transformers import GPT2Tokenizer, GPT2LMHeadModel

def load_model(model_directory):
    model = GPT2LMHeadModel.from_pretrained(model_directory)
    tokenizer = GPT2Tokenizer.from_pretrained(model_directory)
    model.eval()
    return model, tokenizer

def generate_response(tokenizer, model, text, max_length=50):
    inputs = tokenizer.encode(text, return_tensors="pt")
    response = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(response[0], skip_special_tokens=True)

def save_feedback(response_id, feedback_type, user_comment):

    with open('feedback_log.txt', 'a') as file:
        file.write(f"{response_id}, {feedback_type}, {user_comment}\n")
    print(f"Feedback received: {response_id}, {feedback_type}, {user_comment}")
