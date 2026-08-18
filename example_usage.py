from client import FullDuplexStreamingVoiceAgentPipelineClient

def main():
    client = FullDuplexStreamingVoiceAgentPipelineClient()
    res = client.stream_voice_duplex(50, 0.85)
    print(f"Duplex Latency: {res['duplex_latency_ms']}ms")
    print(f"Interruption Handled: {res['interruption_handled']}")
    print(f"Stream Health: {res['stream_health']}")

if __name__ == "__main__":
    main()
