from utils import Session


def query_by_id(model, id):
    session = Session()
    result = session.query(model).get(id)
    session.close()
    return result


def query(model, *criterion):
    session = Session()
    if criterion:
        result = session.query(model).filter(*criterion).all()
    else:
        result = session.query(model).all()
    session.close()
    return result


def delete(model, *criterion):
    session = Session()
    if criterion:
        session.query(model).filter(*criterion).delete()
    session.commit()
    session.close()


def save(model, data, instance=None):
    session = Session()
    if instance is not None:
        for attr, value in data.items():
            setattr(instance, attr, value)
    else:
        instance = model(**data)
    session.add(instance)
    session.commit()
    # session.close()
    return instance
