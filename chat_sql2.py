from azure.identity import InteractiveBrowserCredential
from sqlalchemy import create_engine
from langchain_community.utilities.sql_database import SQLDatabase
import urllib

# Azure SQL details
server = "azsql-svr-prod-cer.database.windows.net"
database = "azsql-db-prod-cer"

# Azure AD token-based auth
credential = InteractiveBrowserCredential()
access_token = credential.get_token("https://database.windows.net/.default").token

# Set up connection string for SQLAlchemy using pyodbc
connection_uri = (
    f"mssql+pyodbc://@{server}/{database}?"
    + urllib.parse.urlencode({
        "driver": "ODBC Driver 17 for SQL Server",
        "authentication": "ActiveDirectoryAccessToken"
    })
)

# Inject access token into SQLAlchemy engine
engine = create_engine(connection_uri, connect_args={"attrs_before": {"AccessToken": access_token}})
#db = SQLDatabase(engine)
db = SQLDatabase(engine, include_tables=["AUMRollingME_Fact_VW"])

