# melite-tts-nodes — the TTS half of the audio-core split (2026-09-04).
# Carved from melite-audio-nodes (the all-in-one was too heavy for a
# master pack): Qwen3-TTS synthesis, voice embeddings, and the Voice
# Studio (.qvoice creation/preview). Class names unchanged — the split
# installs replace the all-in-one without touching graphs.
from .nodes import (LoadAudiocoreModel, UnloadAudiocoreModel,
                    AudiocoreFamilyInfo, AudiocoreTTS,
                    AudiocoreVoiceEmbedding, AudiocoreVoiceStudio)
NODE_CLASS_MAPPINGS = {
    "LoadAudiocoreModel": LoadAudiocoreModel,
    "UnloadAudiocoreModel": UnloadAudiocoreModel,
    "AudiocoreFamilyInfo": AudiocoreFamilyInfo,
    "AudiocoreTTS": AudiocoreTTS,
    "AudiocoreVoiceEmbedding": AudiocoreVoiceEmbedding,
    "AudiocoreVoiceStudio": AudiocoreVoiceStudio,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadAudiocoreModel": "LoadAudiocoreModel (Melite)",
    "UnloadAudiocoreModel": "UnloadAudiocoreModel (Melite)",
    "AudiocoreFamilyInfo": "AudiocoreFamilyInfo (Melite)",
    "AudiocoreTTS": "AudiocoreTTS (Melite)",
    "AudiocoreVoiceEmbedding": "AudiocoreVoiceEmbedding (Melite)",
    "AudiocoreVoiceStudio": "AudiocoreVoiceStudio (Melite)",
}

__all__ = [*NODE_CLASS_MAPPINGS, *NODE_DISPLAY_NAME_MAPPINGS]
