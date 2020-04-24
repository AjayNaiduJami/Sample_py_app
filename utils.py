def as_dict(result):
    return {
        row["id"]: row["value"]
        for row in result
    }