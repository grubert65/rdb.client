# rdb.client
A base class for any DBMS client driver


# Synopsys

    import rdb.client

    # get a client object
    client = rdb.client.get_client(driver = "<an rdb.client driver>")

    try:
        client.connect(**params)    # each client needs to implement this

        records = client.select_as_dict(table= "<A table>")
    except Exception as e:
        print(f"Something went wrong {e}")
