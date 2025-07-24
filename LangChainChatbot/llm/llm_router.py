from config.settings import LLM_PROVIDER

def get_llm_client():
    if LLM_PROVIDER == "huggingface":
        from llm.providers.huggingface_client import HuggingFaceClient
        return HuggingFaceClient()
    elif LLM_PROVIDER == "openai":
        from llm.providers.openai_client import OpenAIClient
        return OpenAIClient()
    elif LLM_PROVIDER == "runpod":
        from llm.providers.runpod_client import RunPodClient
        return RunPodClient()
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")

