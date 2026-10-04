
DEBUG_MODE = False
COLOR_BLOCK = 'gray'
COLOR_BLOCK_OUTLINE = 'black'
COLOR_EMPTY = 'white'
COLOR_GRAPH = 'green'
COLOR_PATH = 'orange'
def get_configurations():
    return {
        "Debug Mode": DEBUG_MODE,
        "Color Block": COLOR_BLOCK,
        "Color Block Outline": COLOR_BLOCK_OUTLINE,
        "Color Empty": COLOR_EMPTY,
        "Color Graph": COLOR_GRAPH,
        "Color Path": COLOR_PATH,
    }
def display_config(config):
    for key, value in config.items():
        print(f"{key}: {value}")
def main():
    config = get_configurations()
    display_config(config)
if __name__ == "__main__":
    main()