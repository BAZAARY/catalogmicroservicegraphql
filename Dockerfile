FROM python:3.9-slim
WORKDIR /code
RUN pip install fastapi uvicorn supabase google-auth PyDrive python-dotenv ariadne starlette
COPY ./ /code/
EXPOSE 8000
# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]