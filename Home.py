import os
from flask import Flask, render_template, request, session, redirect, send_file, url_for
import json
from werkzeug.utils import secure_filename
from DBConnection import Db
from config import FLASK_SECRET_KEY, get_gemini_api_key

app = Flask(__name__, template_folder='template', static_url_path='/static/')

app.secret_key = FLASK_SECRET_KEY


@app.route('/')
def ind():
    return render_template("HomePage.html")


@app.route('/HomePage')
def HomePage():
    return render_template("HomePage.html")


@app.route('/UserHome')
def UserHome():
    try:
        ob = Db()
        alerts = ob.select("SELECT * FROM alerts ORDER BY id DESC LIMIT 5")
        if not alerts:
            alerts = []
            
        prices = ob.select("SELECT * FROM market_prices ORDER BY id DESC")
        if not prices:
            prices = []
            
        brid = session.get('brid')
        if brid:
            local_alerts = ob.select(f"SELECT * FROM local_alerts WHERE branch_id='{brid}' ORDER BY date DESC, id DESC LIMIT 5")
        else:
            local_alerts = []
        if not local_alerts:
            local_alerts = []
    except Exception as e:
        print(f"Error fetching data: {e}")
        alerts = []
        prices = []
    return render_template("User/UserHome.html", alerts=alerts, market_prices=prices, local_alerts=local_alerts)


@app.route('/Login')
def login():
    return render_template("login.html")


@app.route('/Adminhome')
def Adminhome():
    return render_template("AdminHome.html")


@app.route('/Branchhome')
def Branchhome():
    try:
        ob = Db()
        alerts = ob.select("SELECT * FROM alerts ORDER BY id DESC LIMIT 5")
        if not alerts:
            alerts = []
            
        prices = ob.select("SELECT * FROM market_prices ORDER BY id DESC")
        if not prices:
            prices = []
    except Exception as e:
        print(f"Error fetching data: {e}")
        alerts = []
        prices = []
    return render_template("Branchhome.html", alerts=alerts, market_prices=prices)


@app.route('/LogOut')
def logOut():
    return render_template("LogOut.html")


@app.route('/login1', methods=['post'])
def login1():
    name = request.form['un']
    password = request.form['pass']
    session['lid'] = name
    print(name)
    print(password)
    qry = "select * from login where admin_id='" + name + "' and password='" + password + "'"
    ob = Db()
    print(qry)
    try:
        res = ob.selectOne(qry)
        if res is not None:
            print('admin login correct')
            return render_template("AdminHome.html")
        qry = "select * from branch where branch_id='" + name + "' and password='" + password + "'"
        ob = Db()
        print(qry)
        res = ob.selectOne(qry)
        if res is not None:
            return Branchhome()
        qry = "select * from user_register where user_id='" + name + "' and password='" + password + "'"
        ob = Db()
        print(qry)
        res = ob.selectOne(qry)
        brid = res['branch_id']
        session['brid'] = brid
        if res is not None:
            return UserHome()
    except:
        return "<script>alert('invalid');window.location='/';</script>"


# ------------------------------------------------------Admin----------------------------------------------------#
@app.route('/LinkSelectBranch')
def LinkSelectBranch():
    ob = Db()
    data = None
    res = ob.select("select * from district")
    return render_template('SelectBranch.html', data=res)


@app.route('/LinkAfterDistrictSelect')
def LinkAfterDistrictSelect():
    did = request.args.get('id')
    session['did'] = did
    return render_template("AddDepartment.html")


@app.route('/BranchRegistration', methods=['post'])
def BranchRegistration():
    branchid = request.form['TxtBid']
    did = session['did']
    address = request.form['TxtAddress']
    phone = request.form['TxtPhone']
    email = request.form['TxtEmail']
    pincode = request.form['TxtPincode']
    password = request.form['TxtPassword']
    ob = Db()
    q = "insert into branch values('" + branchid + "','" + address + "','" + phone + "','" + email + "','" + pincode + "','" + password + "','" + did + "')"
    ob.insert(q)
    return "<script>alert('Inserted succesfully');window.location='/Adminhome';</script>"


@app.route('/ViewDepartment')
def ViewDepartment():
    ob = Db()
    data = None
    res = ob.select("select branch.*, district.name as district_name from branch join district on branch.iddistrict=district.iddistrict")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Adminhome';</script>"
    return render_template('ViewDepartment.html', data=res)


@app.route('/LinkEditBranch')
def LinkEditBranch():
    id = request.args.get('id')
    ob = Db()
    data = None
    res = ob.selectOne("select * from branch where branch_id='" + id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Adminhome';</script>"
    return render_template('EditDepartment.html', data=res)


@app.route('/EditDepartment', methods=['post'])
def EditDepartment():
    id = request.form['id']
    address = request.form['TxtAddress']
    phone = request.form['TxtPhone']
    email = request.form['TxtEmail']
    pincode = request.form['TxtPincode']
    password = request.form['TxtPassword']
    ob = Db()
    q = "update branch set address='" + address + "',email='" + email + "',phone='" + phone + "',password='" + password + "',pincode='" + pincode + "' where branch_id='" + id + "'"
    ob.update(q)
    return "<script>alert('Updated succesfully');window.location='/Adminhome';</script>"


@app.route('/DeleteBranch')
def DeleteBranch():
    id = request.args.get('id')
    ob = Db()
    q = "delete from branch where branch_id='" + id + "'"
    ob.delete(q)
    return "<script>alert('Deleted succesfully');window.location='/Adminhome';</script>"


@app.route('/ViewFeedback')
def ViewFeedback():
    ob = Db()
    data = None
    res = ob.select("select * from feedback")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Adminhome';</script>"
    return render_template('ViewFeedback.html', data=res)


@app.route('/LinkReplyFeedback')
def LinkReplyFeedback():
    id = request.args.get('id')
    session['fid'] = id
    return render_template("ReplyFeedback.html")


@app.route('/FeedbackReply', methods=['post'])
def FeedbackReply():
    id = session['fid']
    reply = request.form['TxtReply']
    ob = Db()
    q = "update feedback set reply='" + reply + "',reply_date=curdate() where feedback_id='" + id + "'"
    ob.update(q)
    return "<script>alert('Replied Succesfully');window.location='/Adminhome';</script>"


@app.route('/LinkAddSubsidy')
def LinkAddSubsidy():
    return render_template("AddSubsidy.html")


@app.route('/AddSubsidy', methods=['post'])
def AddSubsidy():
    desc = request.form['TxtDesc']
    ob = Db()
    q = "insert into subsidy values(null,curdate(),'" + desc + "')"
    ob.insert(q)
    return "<script>alert('Inserted Succesfully');window.location='/Adminhome';</script>"


@app.route('/LinkEditSubsidy')
def LinkEditSubsidy():
    id = request.args.get('id')
    ob = Db()
    data = None
    res = ob.selectOne("select * from subsidy where idsubsidy='" + id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/ViewSubsidy';</script>"
    return render_template('EditSubsidy.html', data=res)


@app.route('/EditSubsidy', methods=['post'])
def EditSubsidy():
    id = request.form['id']
    description = request.form['description']
    ob = Db()
    q = "update subsidy set description='" + description + "' where idsubsidy='" + id + "'"
    ob.update(q)
    return "<script>alert('Updated succesfully');window.location='/ViewSubsidy';</script>"


@app.route('/ViewSubsidy')
def ViewSubsidy():
    ob = Db()
    data = None
    res = ob.select("select * from subsidy")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Adminhome';</script>"
    return render_template('ViewSubsidy.html', data=res)


@app.route('/DeleteSubsidy')
def DeleteSubsidy():
    id = request.args.get('id')
    ob = Db()
    q = "delete from subsidy where idsubsidy='" + id + "'"
    ob.delete(q)
    return "<script>alert('Deleted Succesfully');window.location='/Adminhome';</script>"


# ----------------------------------------------Branch-------------------------------------#
@app.route('/ViewSubsidyRequest')
def ViewSubsidyRequest():
    ob = Db()
    data = None
    res = ob.select("select * from subsidy")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Branchhome';</script>"
    return render_template('Branch/ViewSubsidy.html', data=res)


@app.route('/ApprovedSubsidy')
def ApprovedSubsidy():
    id = session['lid']
    ob = Db()
    data = None
    res = ob.select("select * from request_subsidy where branch_id='" + id + "' and status='approved'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Branchhome';</script>"
    return render_template('Branch/ViewApprovedSubsidy.html', data=res)


@app.route('/ViewRequest')
def ViewRequest():
    id = session['lid']
    sid = request.args.get('id')
    ob = Db()

    res = ob.select(
        "select * from request_subsidy where branch_id='" + id + "' and idsubsidy='" + sid + "' and status='requested'")
    return render_template('Branch/ViewSubsidyRequest.html', data=res)


@app.route('/UserBookCrop')
def UserBookCrop():
    ob = Db()
    user = ob.selectOne("SELECT branch_id FROM user_register WHERE user_id='{}'".format(session['lid']))
    branch_id = user['branch_id']
    # show crops only from that branch
    crops = ob.select("SELECT * FROM crop ")
    return render_template("User/BookCrop.html", crops=crops)


@app.route('/InsertCropBooking', methods=['POST'])
def InsertCropBooking():
    crop_id = request.form['crop_id']
    user_id = session['lid']
    ob = Db()
    user = ob.selectOne("SELECT branch_id FROM user_register WHERE user_id='{}'".format(user_id))
    branch_id = user['branch_id']
    query = """
        INSERT INTO crop_booking(branch_id, crop_id, user_id, book_date, status, quantity)
        VALUES('{}','{}','{}',CURDATE(),'Pending', '{}')
    """.format(branch_id, crop_id, user_id, 1)
    ob.insert(query)
    return "<script>alert('Crop Booked Successfully');window.location='/UserHome'</script>"


@app.route('/view_crop_booking')
def view_crop_booking():
    user_id = session['lid']
    ob = Db()
    user = ob.select("SELECT c.name, cb.book_date, cb.status, cb.quantity FROM crop_booking AS cb JOIN crop AS c ON cb.crop_id = c.crop_id WHERE cb.user_id='{}' AND cb.status != 'Rejected' ORDER BY cb.crop_booking_id DESC".format(user_id))
    return render_template("User/ViewCropBooking.html", data=user)



@app.route('/register_crop_link', methods=['GET'])
def register_crop_link():
    return render_template("AddCrop.html")


@app.route('/view_crop')
def view_crop():
    db = Db()
    query = "SELECT crop_id, name, description, quantity FROM crop ORDER BY crop_id DESC"
    data = db.select(query)
    return render_template("ViewCrop.html", data=data)


@app.route('/LinkEditCrop')
def LinkEditCrop():
    id = request.args.get('id')
    ob = Db()
    data = None
    res = ob.selectOne("select * from crop where crop_id='" + id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/view_crop';</script>"
    return render_template("EditCrop.html", data=res)


@app.route('/UpdateCrop', methods=['post'])
def UpdateCrop():
    id = request.form['id']
    name = request.form['name']
    description = request.form['description']
    quantity = request.form['quantity']
    ob = Db()
    q = "update crop set name=%s, description=%s, quantity=%s where crop_id=%s"
    ob.update(q, (name, description, quantity, id))
    return "<script>alert('Updated succesfully');window.location='/view_crop';</script>"

@app.route('/fertilizer_insert', methods=['POST'])
def fertilizer_insert():
    name = request.form['TxtName']
    dosage = request.form['TxtDosage']
    purpose = request.form['TxtPurpose']
    db = Db()
    query = "INSERT INTO fertilizer(name, dosage, purpose) VALUES('"+name+"','"+dosage+"','"+purpose+"')"
    db.insert(query)
    return redirect('/fertilizer_register')


@app.route('/fertilizer_register')
def fertilizer_register():
    return render_template("AddFertilizer.html")








@app.route('/view_fertilizer_user')
def view_fertilizer_user():
    db = Db()
    query = "SELECT * FROM fertilizer ORDER BY fertilizer_id DESC"
    data = db.select(query)
    return render_template("User/ViewFertilizer.html", data=data)


@app.route('/LinkEditFertilizer')
def LinkEditFertilizer():
    id = request.args.get('id')
    ob = Db()
    data = None
    res = ob.selectOne("select * from fertilizer where fertilizer_id='" + id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/view_fertilizer';</script>"
    return render_template('EditFertilizer.html', data=res)


@app.route('/EditFertilizer', methods=['post'])
def EditFertilizer():
    id = request.form['id']
    name = request.form['name']
    dosage = request.form['dosage']
    purpose = request.form['purpose']
    ob = Db()
    q = "update fertilizer set name='" + name + "', dosage='" + dosage + "', purpose='" + purpose + "' where fertilizer_id='" + id + "'"
    ob.update(q)
    return "<script>alert('Updated succesfully');window.location='/view_fertilizer';</script>"


@app.route('/view_fertilizer')
def view_fertilizer():
    db = Db()
    query = "SELECT * FROM fertilizer ORDER BY fertilizer_id DESC"
    data = db.select(query)
    return render_template("ViewFertilizer.html", data=data)


@app.route('/delete_fertilizer/<int:id>')
def delete_fertilizer(id):
    db = Db()
    query = "DELETE FROM fertilizer WHERE fertilizer_id=" + str(id)
    db.delete(query)
    return redirect('/view_fertilizer')


@app.route('/delete_crop/<int:id>')
def delete_crop(id):
    db = Db()
    query = "DELETE FROM crop WHERE crop_id= "+str(id)+" "
    db.delete(query )
    return redirect('/view_crop')



@app.route('/register_crop', methods=['POST'])
def register_crop():
    name = request.form['TxtName']
    description = request.form['TxtDesc']
    quantity = request.form['TxtQuantity']
    ob = Db()
    query = """
        INSERT INTO crop(name, description, quantity)
        VALUES(%s, %s, %s)
    """
    ob.insert(query, (name, description, quantity))
    return "<script>alert('Inserted successfully');window.location='/view_crop';</script>"



@app.route('/RejectBooking/<id>')
def RejectBooking(id):
    ob = Db()
    query = "UPDATE crop_booking SET status='Rejected' WHERE crop_booking_id='{}'".format(id)
    ob.update(query)
    return "<script>alert('Booking Rejected');window.location='/BranchViewBooking'</script>"

@app.route('/ApproveBooking', methods=['POST'])
def ApproveBooking():
    booking_id = request.form['booking_id']
    crop_id = request.form['crop_id']
    approved_qty = int(request.form['approved_qty'])
    ob = Db()
    
    # Check if we have enough stock
    crop = ob.selectOne("SELECT quantity FROM crop WHERE crop_id='{}'".format(crop_id))
    try:
        available_qty = int(crop['quantity'])
    except:
        available_qty = 0
        
    if approved_qty > available_qty:
        return "<script>alert('Approved amount cannot easily exceed available stock!');window.location='/BranchViewBooking'</script>"
        
    # Deduct stock and update booking
    new_stock = available_qty - approved_qty
    ob.update("UPDATE crop SET quantity='{}' WHERE crop_id='{}'".format(new_stock, crop_id))
    ob.update("UPDATE crop_booking SET quantity='{}', status='Approved' WHERE crop_booking_id='{}'".format(approved_qty, booking_id))
    
    return "<script>alert('Booking Approved Successfully');window.location='/BranchViewBooking'</script>"



@app.route('/BranchViewBooking')
def BranchViewBooking():
    branch_id = session['lid']
    print(branch_id)
    ob = Db()
    query = """
        SELECT
        cb.crop_booking_id,
        ur.name AS user_name,
        cb.crop_id,
        c.name,
        cb.book_date,
        cb.status,
        cb.quantity AS requested_qty,
        c.quantity AS balance_qty
        FROM crop_booking AS cb
        JOIN crop AS c ON cb.crop_id = c.crop_id
        JOIN user_register AS ur ON cb.user_id = ur.user_id
        WHERE cb.branch_id='{}' AND cb.status='Pending'
        ORDER BY cb.crop_booking_id DESC
    """.format(branch_id)
    data = ob.select(query)
    return render_template("Branch/ViewCropBooking.html", data=data)

@app.route('/BranchApprovedBooking')
def BranchApprovedBooking():
    branch_id = session['lid']
    ob = Db()
    query = """
        SELECT
        cb.crop_booking_id,
        ur.name AS user_name,
        cb.crop_id,
        c.name,
        cb.book_date,
        cb.status,
        cb.quantity
        FROM crop_booking AS cb
        JOIN crop AS c ON cb.crop_id = c.crop_id
        JOIN user_register AS ur ON cb.user_id = ur.user_id
        WHERE cb.branch_id='{}' AND cb.status='Approved'
        ORDER BY cb.crop_booking_id DESC
    """.format(branch_id)
    data = ob.select(query)
    return render_template("Branch/ViewApprovedCropBooking.html", data=data)



@app.route('/ApproveRequest')
def ApproveRequest():
    id = request.args.get('id')
    ob = Db()
    q = "update request_subsidy set status='approved' where idrequest_subsidy='" + id + "'"
    ob.update(q)
    return "<script>alert('Approved Successfully');window.location='/Branchhome';</script>"


@app.route('/RejectRequest')
def RejectRequest():
    id = request.args.get('id')
    ob = Db()
    q = "update request_subsidy set status='rejected' where idrequest_subsidy='" + id + "'"
    ob.update(q)
    return "<script>alert('Rejected Succesfully');window.location='/Branchhome';</script>"


@app.route('/ViewQueries')
def ViewQueries():
    id = session['lid']
    ob = Db()
    data = None
    res = ob.select("select * from queries where branch_id='" + id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Branchhome';</script>"
    return render_template('Branch/ViewQueries.html', data=res)


@app.route('/LinkReplyQuery')
def LinkReplyQuery():
    id = request.args.get('id')
    session['rid'] = id
    return render_template("Branch/ReplyQuery.html")


@app.route('/ReplyQuery', methods=['post'])
def ReplyQuery():
    id = session['rid']
    reply = request.form['TxtReply']
    ob = Db()
    q = "update queries set reply='" + reply + "' where idqueries='" + id + "'"

    ob.update(q)
    return "<script>alert('Replied Succesfully');window.location='/Branchhome';</script>"


@app.route('/BranchViewFarms')
def BranchViewFarms():
    id = session['lid']
    ob = Db()
    data = None
    query = """
        SELECT uf.*, ur.name, ur.phone 
        FROM user_farms uf
        JOIN user_register ur ON uf.user_id = ur.user_id
        WHERE uf.branch_id = '{}' AND uf.status = 'Pending'
    """.format(id)
    res = ob.select(query)
    # Removing alert redirect to render empty table instead
    return render_template('Branch/ViewFarms.html', data=res)


@app.route('/BranchApprovedFarms')
def BranchApprovedFarms():
    id = session['lid']
    ob = Db()
    data = None
    query = """
        SELECT uf.*, ur.name, ur.phone 
        FROM user_farms uf
        JOIN user_register ur ON uf.user_id = ur.user_id
        WHERE uf.branch_id = '{}' AND uf.status = 'Approved'
    """.format(id)
    res = ob.select(query)
    # Removing alert redirect to render empty table instead
    return render_template('Branch/ViewApprovedFarms.html', data=res)


@app.route('/ApproveFarm')
def ApproveFarm():
    id = request.args.get('id')
    ob = Db()
    q = "update user_farms set status='Approved' where farm_id='" + id + "'"
    ob.update(q)
    return "<script>alert('Approved Successfully');window.location='/BranchViewFarms';</script>"


@app.route('/RejectFarm')
def RejectFarm():
    id = request.args.get('id')
    ob = Db()
    q = "update user_farms set status='Rejected' where farm_id='" + id + "'"
    ob.update(q)
    return "<script>alert('Rejected Successfully');window.location='/BranchViewFarms';</script>"


@app.route('/BranchViewUsers')
def BranchViewUsers():
    id = session['lid']
    ob = Db()
    data = None
    query = "SELECT * FROM user_register WHERE branch_id = '{}'".format(id)
    res = ob.select(query)
    return render_template('Branch/ViewUsers.html', data=res)


# -----------------------------------------------------User-----------------------------------------------------------#
@app.route('/LinkAddUser')
def LinkAddUser():
    id = request.args.get('id')
    session['bid'] = id
    return render_template('User/UserRegister.html')


@app.route('/UserRegistration', methods=['post'])
def UserRegistration():
    userid = request.form['TxtUserid']
    name = request.form['TxtName']
    address = request.form['TxtAddress']
    phone = request.form['TxtPhone']
    password = request.form['TxtPassword']
    branchid = session['bid']
    ob = Db()
    res = ob.select("select * from user_register where user_id='" + str(userid) + "'")
    if res:
        return "<script>alert('Id Already Exists ');window.location='/Login';</script>"
    else:
        q = "insert into user_register values('" + userid + "','" + name + "','" + address + "','" + phone + "','" + password + "','" + branchid + "')"
        ob.insert(q)
        return "<script>alert('Inserted successfully');window.location='/Login';</script>"


@app.route('/ViewDistrict')
def ViewDistrict():
    ob = Db()
    data = None
    res = ob.select("select * from district")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Branchhome';</script>"
    return render_template('User/ViewDistrict.html', data=res)


@app.route('/ViewbranchUser')
def ViewbranchUser():
    id = request.args.get('id')
    ob = Db()
    data = None
    res = ob.select("select * from branch where iddistrict='" + id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/Login';</script>"
    return render_template('User/ViewbranchUser.html', data=res)


@app.route('/UserViewBranches')
def UserViewBranches():
    ob = Db()
    data = None
    res = ob.select("select * from branch")
    
    # Get the user's current branch id
    user_id = session.get('lid')
    current_branch_id = None
    if user_id:
        user_res = ob.selectOne(f"select branch_id from user_register where user_id='{user_id}'")
        if user_res:
            current_branch_id = user_res['branch_id']

    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/UserHome';</script>"
        
    return render_template('User/UserViewBranches.html', data=res, current_branch_id=current_branch_id)


@app.route('/ChangeBranch')
def ChangeBranch():
    id = request.args.get('id')
    user_id = session['lid']
    ob = Db()
    q = "update user_register set branch_id=%s where user_id=%s"
    ob.update(q, (id, user_id))
    return "<script>alert('Updated succesfully');window.location='/UserViewBranches';</script>"


@app.route('/UserProfile')
def UserProfile():
    id = session.get('lid')
    ob = Db()
    res = ob.selectOne(f"select * from user_register where user_id='{id}'")
    if res:
        return render_template('User/UserProfile.html', data=res)
    else:
        return "<script>alert('Failed to fetch profile details');window.location='/UserHome';</script>"

@app.route('/EditProfile', methods=['POST'])
def EditProfile():
    id = request.form['user_id']
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    password = request.form['password']
    
    ob = Db()
    if session.get('lid') != id:
        return "<script>alert('Unauthorized');window.location='/UserHome';</script>"
        
    query = "update user_register set name='{}', phone='{}', address='{}', password='{}' where user_id='{}'".format(name, phone, address, password, id)
    ob.update(query)
        
    return "<script>alert('Profile updated successfully');window.location='/UserProfile';</script>"


@app.route('/ViewSubsidyUser')
def ViewSubsidyUser():
    ob = Db()
    data = None
    res = ob.select("select * from subsidy")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/UserHome';</script>"
    return render_template('User/ViewSubsidyUser.html', data=res)


@app.route('/LinkSendRequest')
def LinkSendRequest():
    id = request.args.get('id')
    session['sid'] = id
    return render_template("User/SendSubsidyRequest.html")


@app.route('/SendSubsidyRequest', methods=['post'])
def SendSubsidyRequest():
    sid = session['sid']
    userid = session['lid']
    brid = str(session['brid'])
    desc = request.form['TxtDesc']
    ob = Db()
    q = "insert into request_subsidy values(null,'" + userid + "',curdate(),'" + desc + "','" + sid + "','requested','" + brid + "')"
    ob.insert(q)
    return "<script>alert('Inserted succesfully');window.location='/UserHome';</script>"


@app.route('/ViewSubsidyStatus')
def ViewSubsidyStatus():
    user_id = session['lid']
    ob = Db()
    data = None
    res = ob.select(f"SELECT rs.*, s.description AS subsidy_name FROM request_subsidy rs JOIN subsidy s ON rs.idsubsidy = s.idsubsidy WHERE rs.user_id='{user_id}'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/UserHome';</script>"
    return render_template('User/ViewSubsidyStatus.html', data=res)


@app.route('/LinkRegisterFarm')
def LinkRegisterFarm():
    return render_template("User/RegisterFarm.html")


@app.route('/download')
def download():
    id = request.args.get('id')
    path = "\\static\\"+id
    fi   = os.getcwd()+path
    print(fi)
    return send_file(fi, as_attachment=True)


@app.route('/FarmRegistration', methods=['post'])
def FarmRegistration():
    userid = session['lid']
    farmaddress = request.form['TxtFarmAddress']
    farmdetails = request.form['TxtFarmDetails']

    i = request.files['image']
    name = secure_filename(i.filename)
    i.save(os.path.join('static', name))

    ob = Db()
    user = ob.selectOne("select branch_id from user_register where user_id='" + userid + "'")
    branchid = user['branch_id']
    q = "insert into user_farms (user_id, date_of_register, farm_address, farm_details, farm_image, branch_id, status) values('" + userid + "',curdate(),'" + farmaddress + "','" + farmdetails + "','" + name + "','" + branchid + "','Pending')"
    ob.insert(q)
    return "<script>alert('Inserted successfully');window.location='/UserHome';</script>"


@app.route('/LinkSendQuery')
def LinkSendQuery():
    return render_template("User/SendQuery.html")



@app.route('/search_branch_link')
def search_branch_link():
    return render_template("User/SearchBranch.html")


@app.route('/SendQuery', methods=['post'])
def SendQuery():
    userid = session['lid']
    brid = session['brid']
    query = request.form['TxtQuery']
    ob = Db()
    q = "insert into queries values(null,'" + userid + "','" + query + "','','" + brid + "')"
    ob.insert(q)
    return "<script>alert('Inserted succesfully');window.location='/UserHome';</script>"


@app.route('/ViewQuery')
def ViewQuery():
    user_id = session['lid']
    ob = Db()
    data = None
    res = ob.select("select * from queries where user_id='" + user_id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/UserHome';</script>"
    return render_template('User/ViewQuery.html', data=res)


@app.route('/search_branch', methods=['post'])
def search_branch():
    data = request.form['txtSearch'].strip()
    ob = Db()
    res = ob.select("select * from branch where address like %s or branch_id like %s", ("%" + data + "%", "%" + data + "%"))
    if not res:
        return "<script>alert('No Data Found');window.location='/search_branch_link';</script>"
    return render_template('User/SearchResult.html', data=res)


@app.route('/ViewFarm')
def ViewFarm():
    user_id = session['lid']
    ob = Db()
    data = None
    res = ob.select("select * from user_farms where user_id='" + user_id + "'")
    if res:
        data = res
    return render_template('User/ViewFarm.html', data=res)


@app.route('/deletefarm')
def deletefarm():
    id = request.args.get('id')
    ob = Db()
    q = "delete from user_farms where farm_id='" + id + "' "
    ob.delete(q)
    return "<script>alert('Deleted succesfully');window.location='/UserHome';</script>"


@app.route('/LinkSendFeedback')
def LinkSendFeedback():
    return render_template("User/SendFeedback.html")


@app.route('/SendFeedback', methods=['post'])
def SendFeedback():
    userid = session['lid']
    feedback = request.form['TxtFeedback']
    ob = Db()
    q = "insert into feedback values(null, %s, curdate(), %s, '', '')"
    ob.insert(q, (userid, feedback))
    return "<script>alert('Inserted succesfully');window.location='/UserHome';</script>"


@app.route('/ViewFeedbackUser')
def ViewFeedbackUser():
    user_id = session['lid']
    ob = Db()
    data = None
    res = ob.select("select * from feedback where user_id='" + user_id + "'")
    if res:
        data = res
    if data == None:
        return "<script>alert('No Data Found');window.location='/UserHome';</script>"
    return render_template('User/ViewFeedback.html', data=res)


# Upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/detect_disease_gemini', methods=['GET', 'POST'])
def detect_disease_gemini():
    context = {}
    if request.method == "POST":
        leaf_image = request.files.get('leaf_image')
        api_key = get_gemini_api_key("GEMINI_DISEASE_API_KEY")
        if not api_key:
            context['error'] = "Gemini API key is not configured. Set GEMINI_API_KEY in your .env file."
            return render_template("User/GeminiDiseaseDetect.html", **context)

        if leaf_image and leaf_image.filename != "":
            from werkzeug.utils import secure_filename
            import os
            import base64
            import urllib.request
            import urllib.error
            import json

            try:
                filename = secure_filename(leaf_image.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                leaf_image.save(file_path)
                
                context["image_url"] = url_for('static', filename='uploads/' + filename)

                # Read image and encode to base64
                with open(file_path, "rb") as image_file:
                    img_data = image_file.read()
                    
                img_b64 = base64.b64encode(img_data).decode('utf-8')
                mime_type = leaf_image.content_type if leaf_image.content_type else "image/jpeg"

                # Prepare payload for Gemini API
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
                payload = {
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": 'Analyze the uploaded image of a plant/leaf. Identify any disease. Return a JSON object ONLY with the following exact keys: "disease_name", "details", "confidence_level" (a string between 0% to 100%), "reason", "preventions", "medicines_or_fertilizers", "more_details". If no plant or disease is detected, state that clearly in the fields.'
                                },
                                {
                                    "inline_data": {
                                        "mime_type": mime_type,
                                        "data": img_b64
                                    }
                                }
                            ]
                        }
                    ],
                    "generationConfig": {
                        "responseMimeType": "application/json"
                    }
                }

                headers = {"Content-Type": "application/json"}
                req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')

                with urllib.request.urlopen(req) as response:
                    res_body = response.read()
                    res_json = json.loads(res_body)

                    text_response = res_json['candidates'][0]['content']['parts'][0]['text']

                    # Safe parsing
                    try:
                        parsed_result = json.loads(text_response.strip())
                        context['result'] = parsed_result
                        
                        try:
                            ob = Db()
                            user_id = session.get('lid', 'guest')
                            d_name = parsed_result.get('disease_name', 'Unknown')
                            conf = str(parsed_result.get('confidence_level', 'Unknown'))
                            if d_name and d_name.lower() not in ['none', 'healthy', 'unknown', 'n/a']:
                                q = "INSERT INTO disease_prediction (user_id, disease_name, confidence, prediction_date) VALUES (%s, %s, %s, curdate())"
                                ob.insert(q, (str(user_id), str(d_name), conf))
                        except Exception as e:
                            print("DB Insert Error:", e)

                    except json.JSONDecodeError as decode_error:
                        context['error'] = f"Failed to parse AI output: {text_response}"

            except urllib.error.HTTPError as e:
                error_body = e.read().decode('utf-8')
                try:
                    error_json = json.loads(error_body)
                    context['error'] = f"API Error: {error_json.get('error', {}).get('message', str(e))}"
                except:
                    context['error'] = f"API Error HTTP {e.code}: {e.reason}"
            except Exception as e:
                context['error'] = f"An unexpected error occurred: {str(e)}"

    return render_template("User/GeminiDiseaseDetect.html", **context)


@app.route('/crop_advisor_gemini', methods=['GET', 'POST'])
def crop_advisor_gemini():
    context = {}
    if request.method == 'POST':
        location = request.form.get('location', '')
        soil_type = request.form.get('soil_type', '')
        season = request.form.get('season', '')
        land_size = request.form.get('land_size', '')

        context['user_input'] = {
            'location': location,
            'soil_type': soil_type,
            'season': season,
            'land_size': land_size
        }

        api_key = get_gemini_api_key("GEMINI_ADVISOR_API_KEY")
        if not api_key:
            context['error'] = "Gemini API key is not configured. Set GEMINI_API_KEY in your .env file."
            return render_template('User/GeminiCropAdvisor.html', **context)

        import urllib.request
        import urllib.error
        import json

        try:
            # Prepare payload for Gemini API
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            
            prompt_text = f'Act as an expert agricultural advisor. Based on the following farm parameters - Location: "{location}", Soil Type: "{soil_type}", Season: "{season}", Land Size: "{land_size} acres" - recommend the best high-yield crops to grow. Return a JSON object ONLY with the following exact keys: "recommended_crops" (a comma separated list), "expected_yield", "required_fertilizers", "estimated_cost" (including estimated profits if possible), "farming_tips" (a helpful paragraph of expert advice). Do not include any extra text.'
            
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt_text
                            }
                        ]
                    }
                ],
                "generationConfig": {
                    "responseMimeType": "application/json"
                }
            }

            headers = {"Content-Type": "application/json"}
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')

            with urllib.request.urlopen(req) as response:
                res_body = response.read()
                res_json = json.loads(res_body)

                text_response = res_json['candidates'][0]['content']['parts'][0]['text']

                # Safe parsing
                try:
                    parsed_result = json.loads(text_response.strip())
                    context['result'] = parsed_result
                except json.JSONDecodeError as decode_error:
                    context['error'] = f"Failed to parse AI output: {text_response}"

        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            context['error'] = f"API Error: {error_body}"
        except urllib.error.URLError as e:
            context['error'] = f"Network Error: Failed to connect to Gemini API. Details: {e.reason}"
        except Exception as e:
            context['error'] = f"An unexpected error occurred: {str(e)}"

    return render_template('User/GeminiCropAdvisor.html', **context)


@app.route('/farming_guide_gemini', methods=['GET', 'POST'])
def farming_guide_gemini():
    context = {}
    ob = Db()
    # Fetch all crops for the dropdown
    crops = ob.select("SELECT name FROM crop ORDER BY name ASC")
    context['crops'] = crops

    if request.method == 'POST':
        crop_name = request.form.get('crop_name', '')
        context['selected_crop'] = crop_name

        api_key = get_gemini_api_key("GEMINI_GUIDE_API_KEY")
        if not api_key:
            context['error'] = "Gemini API key is not configured. Set GEMINI_API_KEY in your .env file."
            return render_template('User/GeminiFarmingGuide.html', **context)

        import urllib.request
        import urllib.error
        import json

        try:
            # Prepare payload for Gemini API
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            
            prompt_text = f'Act as an expert agricultural advisor. Provide a complete, highly detailed farming guide for cultivating "{crop_name}". Return a JSON object ONLY with the following exact keys: "planting_details", "seasons", "watering", "soil_and_fertilizers", "full_guide" (a lengthy step-by-step summary). Do not include any extra text.'
            
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt_text
                            }
                        ]
                    }
                ],
                "generationConfig": {
                    "responseMimeType": "application/json"
                }
            }

            headers = {"Content-Type": "application/json"}
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')

            with urllib.request.urlopen(req) as response:
                res_body = response.read()
                res_json = json.loads(res_body)

                text_response = res_json['candidates'][0]['content']['parts'][0]['text']

                # Safe parsing
                try:
                    parsed_result = json.loads(text_response.strip())
                    context['result'] = parsed_result
                except json.JSONDecodeError as decode_error:
                    context['error'] = f"Failed to parse AI output: {text_response}"

        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            context['error'] = f"API Error: {error_body}"
        except urllib.error.URLError as e:
            context['error'] = f"Network Error: Failed to connect to Gemini API. Details: {e.reason}"
        except Exception as e:
            context['error'] = f"An unexpected error occurred: {str(e)}"

    return render_template('User/GeminiFarmingGuide.html', **context)


@app.route('/AdminDiseaseAnalytics')
def AdminDiseaseAnalytics():
    ob = Db()
    
    # Get disease distribution
    q_dist = "SELECT disease_name, COUNT(*) as count FROM disease_prediction GROUP BY disease_name ORDER BY count DESC LIMIT 10"
    dist_data = ob.select(q_dist)
    if not dist_data:
        dist_data = []
        
    # Get total predictions
    q_total = "SELECT COUNT(*) as total FROM disease_prediction"
    total_data = ob.selectOne(q_total)
    total_predictions = total_data['total'] if total_data else 0
    
    return render_template('AdminDiseaseAnalytics.html', dist_data=dist_data, total_predictions=total_predictions)

@app.route('/AdminManageAlerts')
def AdminManageAlerts():
    ob = Db()
    res = ob.select("SELECT * FROM alerts ORDER BY id DESC")
    return render_template('AdminManageAlerts.html', data=res)


@app.route('/AdminAddAlert', methods=['POST'])
def AdminAddAlert():
    title = request.form['title']
    message = request.form['message']
    type_ = request.form['type']
    
    ob = Db()
    q = "INSERT INTO alerts (title, message, type, date) VALUES (%s, %s, %s, curdate())"
    ob.insert(q, (title, message, type_))
    return "<script>alert('Alert Broadcasted Successfully');window.location='/AdminManageAlerts';</script>"


@app.route('/DeleteAlert')
def DeleteAlert():
    id = request.args.get('id')
    ob = Db()
    q = "DELETE FROM alerts WHERE id='" + str(id) + "'"
    ob.delete(q)
    return "<script>alert('Alert Deleted Successfully');window.location='/AdminManageAlerts';</script>"

@app.route('/LinkEditAlert')
def LinkEditAlert():
    id = request.args.get('id')
    ob = Db()
    res = ob.selectOne("SELECT * FROM alerts WHERE id='" + str(id) + "'")
    return render_template('EditAlert.html', data=res)

@app.route('/EditAlert', methods=['POST'])
def EditAlert():
    id = request.form['id']
    title = request.form['title']
    message = request.form['message']
    type_ = request.form['type']
    
    ob = Db()
    q = "UPDATE alerts SET title=%s, message=%s, type=%s WHERE id=%s"
    ob.update(q, (title, message, type_, id))
    return "<script>alert('Alert Updated Successfully');window.location='/AdminManageAlerts';</script>"

# ---------------- MARKET PRICE BROADCASTER ---------------- #

@app.route('/AdminManagePrices')
def AdminManagePrices():
    ob = Db()
    res = ob.select("SELECT * FROM market_prices ORDER BY id DESC")
    return render_template('AdminManagePrices.html', data=res)

@app.route('/AdminAddPrice', methods=['POST'])
def AdminAddPrice():
    item_name = request.form['item_name']
    category = request.form['category']
    price = request.form['price']
    unit = request.form['unit']
    
    ob = Db()
    q = "INSERT INTO market_prices (item_name, category, price, unit, date) VALUES (%s, %s, %s, %s, curdate())"
    ob.insert(q, (item_name, category, price, unit))
    return "<script>alert('Market Price Broadcasted Successfully');window.location='/AdminManagePrices';</script>"

@app.route('/DeletePrice')
def DeletePrice():
    id = request.args.get('id')
    ob = Db()
    q = "DELETE FROM market_prices WHERE id='" + str(id) + "'"
    ob.delete(q)
    return "<script>alert('Price Deleted Successfully');window.location='/AdminManagePrices';</script>"

@app.route('/LinkEditPrice')
def LinkEditPrice():
    id = request.args.get('id')
    ob = Db()
    res = ob.selectOne("SELECT * FROM market_prices WHERE id='" + str(id) + "'")
    return render_template('EditPrice.html', data=res)

@app.route('/EditPrice', methods=['POST'])
def EditPrice():
    id = request.form['id']
    item_name = request.form['item_name']
    category = request.form['category']
    price = request.form['price']
    unit = request.form['unit']
    
    ob = Db()
    q = "UPDATE market_prices SET item_name=%s, category=%s, price=%s, unit=%s WHERE id=%s"
    ob.update(q, (item_name, category, price, unit, id))
    return "<script>alert('Market Price Updated Successfully');window.location='/AdminManagePrices';</script>"

# ---------------- PLATFORM REPORTS ---------------- #
import csv
import io
from flask import Response

@app.route('/AdminReports')
def AdminReports():
    return render_template('AdminReports.html')

def get_report_data(report_type, time_range):
    ob = Db()
    date_filter = ""
    # Since `date_of_register`, `request_date` etc are stored as VARCHAR in format 'YYYY-MM-DD'
    if time_range == "Year":
        date_filter = " WHERE LEFT(date_col, 4) = YEAR(CURDATE()) "
    elif time_range == "Quarter":
        date_filter = " WHERE QUARTER(STR_TO_DATE(date_col, '%Y-%m-%d')) = QUARTER(CURDATE()) AND LEFT(date_col, 4) = YEAR(CURDATE()) "
    elif time_range == "Month":
        date_filter = " WHERE MONTH(STR_TO_DATE(date_col, '%Y-%m-%d')) = MONTH(CURDATE()) AND LEFT(date_col, 4) = YEAR(CURDATE()) "

    if report_type == "farming":
        q = "SELECT u.name as 'Farmer Name', u.phone as 'Phone', uf.farm_address as 'Farm Address', uf.date_of_register as 'Registration Date' FROM user_farms uf JOIN user_register u ON uf.user_id = u.user_id"
        if date_filter: q += date_filter.replace("date_col", "uf.date_of_register")
        q += " ORDER BY uf.farm_id DESC"
        
    elif report_type == "subsidies":
        q = "SELECT sr.request_date as 'Date Request', u.name as 'Farmer Name', s.description as 'Subsidy Program' FROM request_subsidy sr JOIN user_register u ON sr.user_id = u.user_id JOIN subsidy s ON sr.idsubsidy = s.idsubsidy WHERE sr.status = 'approved'"
        if date_filter: q += date_filter.replace("WHERE", "AND").replace("date_col", "sr.request_date")
        q += " ORDER BY sr.idrequest_subsidy DESC"
        
    elif report_type == "branch":
        # branch doesn't have a reliable date field in this simple query, so ignoring time_range for branch snapshot
        q = "SELECT b.branch_id as 'Branch Name', b.email as 'Branch Email', b.address as 'Location', COUNT(u.user_id) as 'Registered Farmers' FROM branch b LEFT JOIN user_register u ON b.branch_id = u.branch_id GROUP BY b.branch_id"
        
    else:
        return []
    
    try:
        return ob.select(q)
    except Exception as e:
        print("Report Query Error:", e)
        return []

@app.route('/AdminGenerateReport', methods=['POST'])
def AdminGenerateReport():
    report_type = request.form.get('report_type')
    time_range = request.form.get('time_range')
    data = get_report_data(report_type, time_range)
    
    title = f"{report_type.capitalize()} Report ({time_range})"
    if not data:
        columns = []
    else:
        columns = list(data[0].keys())
        
    return render_template('AdminReportView.html', data=data, columns=columns, title=title, report_type=report_type, time_range=time_range)

@app.route('/AdminDownloadCSV', methods=['POST'])
def AdminDownloadCSV():
    report_type = request.form.get('report_type')
    time_range = request.form.get('time_range')
    data = get_report_data(report_type, time_range)
    
    si = io.StringIO()
    cw = csv.writer(si)
    
    if data:
        columns = list(data[0].keys())
        cw.writerow(columns)
        for row in data:
            cw.writerow([row[col] for col in columns])
    else:
        cw.writerow(["No data matched criteria"])
        
    output = si.getvalue()
    filename = f"{report_type}_report_{time_range}.csv"
    
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-disposition":
                 f"attachment; filename={filename}"}
    )

# ------------------------------------------------------LOCAL ALERTS (BRANCH)----------------------------------------------------#

@app.route('/BranchManageAlerts')
def BranchManageAlerts():
    ob = Db()
    bid = session.get('lid')
    res = ob.select(f"SELECT * FROM local_alerts WHERE branch_id='{bid}' ORDER BY date DESC, id DESC")
    return render_template("BranchManageAlerts.html", data=res)

@app.route('/BranchAddAlert_post', methods=['post'])
def BranchAddAlert_post():
    title = request.form['title']
    message = request.form['message']
    alert_type = request.form['type']
    bid = session.get('lid')
    ob = Db()
    qry = f"INSERT INTO local_alerts (branch_id, title, message, type, date) VALUES ('{bid}', '{title}', '{message}', '{alert_type}', CURDATE())"
    ob.insert(qry)
    return "<script>alert('Local Alert Broadcasted Successfully');window.location='/BranchManageAlerts';</script>"

@app.route('/LinkEditLocalAlert')
def LinkEditLocalAlert():
    alert_id = request.args.get('id')
    ob = Db()
    res = ob.selectOne(f"SELECT * FROM local_alerts WHERE id='{alert_id}'")
    return render_template("BranchEditAlert.html", data=res)

@app.route('/EditLocalAlert_post', methods=['post'])
def EditLocalAlert_post():
    alert_id = request.form['id']
    title = request.form['title']
    message = request.form['message']
    alert_type = request.form['type']
    ob = Db()
    qry = f"UPDATE local_alerts SET title='{title}', message='{message}', type='{alert_type}', date=CURDATE() WHERE id='{alert_id}'"
    ob.update(qry)
    return "<script>alert('Local Alert Updated');window.location='/BranchManageAlerts';</script>"

@app.route('/DeleteLocalAlert')
def DeleteLocalAlert():
    alert_id = request.args.get('id')
    ob = Db()
    ob.delete(f"DELETE FROM local_alerts WHERE id='{alert_id}'")
    return "<script>alert('Local Alert Deleted');window.location='/BranchManageAlerts';</script>"

if __name__ == "__main__":
    app.run(debug=True)
