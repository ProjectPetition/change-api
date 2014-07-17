def change_db():

    from . import changeDB

    return changeDB()

def pet_Body_DB():

    from . import petBodyDB

    return petBodyDB.Body_DB()

def petition_organization_db():

    from . import petOrgDB

    return petOrgDB.Org_DB()

def petition_reasons_db():

    from . import petResDB

    return petResDB.Reasons_DB

def petition_signagures_db():

    from . import petSigDB

    return petSigDB.Signature_DB

def petition_targ_db():

    from . import petTargDB

    return petTargDB.Targ_DB()

def petition_users_db():

    from . import petUsersDB

    return petUsersDB.Users_DB()


