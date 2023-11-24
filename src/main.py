import os

# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()

def main():
    my_input = os.environ["INPUT_BUILD_PLATFORM"]
    sa_key = os.environ["INPUT_GDRIVE-SA-KEY"]
    print(f"SA_KEY: {sa_key}")

    my_output = f'Hello {my_input}'
    print(f"Hello {my_input}")

    set_github_action_output('myOutput', my_output)


if __name__ == "__main__":
    main()
