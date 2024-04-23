from sqlalchemy import create_engine, text

# Define the PostgreSQL connection string
pgsql_data = "postgresql://joviancareers_zmpb_user:fdliuVsnjQ7kn82aa2Juuq9vU6d6k57J@dpg-coj8ufol6cac739t4gpg-a.oregon-postgres.render.com:5432/joviancareers_zmpb"

# Create the SQLAlchemy engine
engine = create_engine(pgsql_data)

def load_jobs_from_db():
    # Attempt to connect to the database
    with engine.connect() as conn:
        # If the connection is successful, print a success message
        print("Connection to PostgreSQL database successful!")
        result = conn.execute(text("SELECT * FROM jobs"))

        result_dict = []

        for row in result.all():
            result_dict.append({
                'id': row[0],
                'title': row[1],
                'location': row[2],
                'salary': row[3],
                'currency': row[4],
                'description': row[5],
                'qualifications': row[6],
                'created_at': row[7],
                'updated_at': row[8]
            })
    return result_dict