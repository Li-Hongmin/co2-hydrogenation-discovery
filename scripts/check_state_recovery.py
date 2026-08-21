from co2_discovery.state_recovery import published_s1_s3_s4_recovery


if __name__ == "__main__":
    for key, value in published_s1_s3_s4_recovery().items():
        print(f"{key}: {value:.6f}")
