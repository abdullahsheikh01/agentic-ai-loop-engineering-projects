POLL_INTERVAL=${1:-60} # Defaults to 60 seconds as required
MARKER_FILE=".task_done"
RESULT_FILE="output.txt"

# Clean up previous runs
rm -f "$MARKER_FILE" "$RESULT_FILE"

echo "🚀 Starting long-running task in the background..."

# 1. Start long task asynchronously in the background
(
  echo "Task running..." 
  sleep 180 # Simulating a 3-minute task (adjust as needed)
  echo "Task finished successfully at $(date)" > "$RESULT_FILE"
  touch "$MARKER_FILE" # Signal completion
) &

TASK_PID=$!
echo "Task started with PID: $TASK_PID"
echo "Entering in-session polling loop (checking every ${POLL_INTERVAL}s)..."

# 2. In-session loop
while true; do
  if [ -f "$MARKER_FILE" ]; then
    echo -e "\n🎉 [SUCCESS] The long task has finished!"
    echo "Content of output file:"
    cat "$RESULT_FILE"
    
    # Clean up marker and exit cleanly
    rm -f "$MARKER_FILE"
    exit 0
  fi

  echo -n "."
  sleep "$POLL_INTERVAL"
done