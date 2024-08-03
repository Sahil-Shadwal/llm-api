# Hosting an LLM as an API

This project demonstrates how to host a Language Model (LLM) as an API using FastAPI and Uvicorn.

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Hosting_an_LLM_as_an_API
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root and specify the model name:

   ```plaintext
   MODEL_NAME=llama3.1
   ```

## Running the API

1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Expose the server using ngrok (optional):**

   ```bash
   ngrok http 8000
   ```

## Example Request

Send a POST request to the `/generate/` endpoint with a JSON payload:

```json
{
  "prompt": "Tell me a story"
}
```
