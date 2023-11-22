#!/bin/sh -l

# Use INPUT_<INPUT_NAME> to get the value of an input
START_MESSAGE="Using build platform: $INPUT_BUILD_PLATFORM"

# Use workflow commands to do things like set debug messages
echo "::notice file=entrypoint.sh,line=7::$GREETING"
echo "$START_MESSAGE"

# Write outputs to the $GITHUB_OUTPUT file
# echo "greeting=$GREETING" >> "$GITHUB_OUTPUT"

exit 0
