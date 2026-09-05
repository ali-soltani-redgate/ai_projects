
## Problem Description

- We want to find LinkedIn jobs that a CV matches
- This would include two parts:
  - Get jobs from LinkedIn via a MCP server
    - We need to pass filter options like location and type of job such as remote or hybrid to the server and get the list of job
    - Then check each job with a LLM to see how much it matches

## Implementation

### Step 1: Create an 