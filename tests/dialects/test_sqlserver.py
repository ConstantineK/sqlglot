def test_sql_server(self):
    self.validate(
        "CREATE TABLE z (n1 FLOAT, n2 FLOAT, n3 FLOAT)",
        "CREATE TABLE z (n1 REAL, n2 REAL, n3 REAL)",
        read="sqlserver",
        write="sqlite",
    )
    self.validate(
        "CREATE TABLE z (n1 INTEGER, n2 INTEGER(10), n3 REAL(8), c1 VARCHAR(30))",
        "CREATE TABLE z (n1 BIGINT, n2 BIGINT, n3 FLOAT(8), c1 VARCHAR(30))",
        read="sqlite",
        write="sqlserver",
    )
    self.validate(
        "SELECT TOP 10 x FROM y",
        "SELECT x FROM y LIMIT 10",
        read="sqlserver",
        write="sqlite"
    )