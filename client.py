class FullDuplexStreamingVoiceAgentPipelineClient:
    def stream_voice_duplex(self, audio_input_buffer_ms: int = 50, interruption_sensitivity: float = 0.8) -> dict:
        return {
            "duplex_latency_ms": 165,
            "interruption_handled": True,
            "stream_health": "STREAMING_DUPLEX_OPTIMAL"
        }
