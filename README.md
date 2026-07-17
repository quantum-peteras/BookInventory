# Peter Turkson Asamoah's Book Inventory

So its basically a fastapi service for a book inventory.

Design and implementation created by Peter Kofi Turkson Asamoah.

Pls Create a .env and add the following variables to it:
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>

Instructions: 
Assignment Requirements

Your submission should include the following:

    System Overview.
        Provide a high-level overview of the proposed Book Inventory System.
        Include a diagram illustrating the architecture and workflow of the system, showing how users interact with the API and how requests flow through the application.
    Database Design
        Design and present the database schema for the system.

        The primary entity should follow the structure below:

        Book
        ----
        id
        title
        author
        num_of_pages


    API Design
        Design the REST API endpoints required to support the following operations:
            Add a book
            Edit a book
            Delete a book
            Get a single book
            Get all books
        Specify the HTTP methods, endpoint URLs, request payloads, and expected responses.
    Project Structure
        Propose a clean and scalable FastAPI project structure, organizing components such as routers, models, schemas, services, database configuration, and utilities.
    Implementation
        Implement the Book Inventory System using FastAPI following your proposed design.
        Ensure the API supports all the required CRUD operations and follows clean coding practices.

Submission

Please submit your completed assignment no later than 1:00 PM tomorrow. Ensure your work is well organized, properly documented, and demonstrates your understanding of FastAPI, API design, and database modeling.

If you have any questions or require clarification, feel free to reach out before the submission deadline.

