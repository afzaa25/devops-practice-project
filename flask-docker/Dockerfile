FROM python:3

RUN pip install flask

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
CMD flask run --host=0.0.0.0