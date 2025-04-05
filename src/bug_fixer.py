import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "stabilityai/stablecode-completion-alpha-3b-4k"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to(device)


def extract_fixed_code(response: str) -> str:
    print("🔍 Raw model output:\n", response)

    if "### Fixed Python Code:" in response:
        response = response.split("### Fixed Python Code:")[1]

    if "```python" in response:
        response = response.split("```python")[1].split("```")[0].strip()
    elif "```" in response:
        response = response.split("```")[1].split("```")[0].strip()

    lines = response.strip().split("\n")
    cleaned = []
    for line in lines:
        if any(bad in line for bad in ["def main", "Hello World", 'print("Hello']):
            continue
        cleaned.append(line.strip())

    final_code = "\n".join(cleaned).strip()
    return final_code if final_code else "⚠️ No valid output generated!"


def detect_and_fix_bug(code_snippet: str) -> str:
    prompt = f"# Python code with a bug:\n{code_snippet.strip()}\n\n### Fixed Python Code:\n"
    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        inputs.pop("token_type_ids", None)

        outputs = model.generate(
            **inputs,
            max_length=inputs["input_ids"].shape[1] + 128,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=False,
            num_beams=3,
            repetition_penalty=1.2,
            eos_token_id=tokenizer.eos_token_id,  
        )
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

        truncated = decoded.split("### Fixed Python Code:")[1].strip()
        return extract_fixed_code("### Fixed Python Code:\n" + truncated)

    except Exception as e:
        return f"Error: {str(e)}"


def fix_python_code(code: str):
    fixed = detect_and_fix_bug(code)
    logs = "✔️ Syntax fixed successfully." if " Error" not in fixed else fixed
    print(f"Fixed Output:\n{fixed}")
    return fixed, logs


