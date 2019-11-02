from builtins import Exception, len
#import mysql.connector
import pymysql

NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="courses"
# )
mydb = pymysql.connect(host='127.0.0.1', port=3306, user='watches',
    password='watches', db='watches', charset="utf8")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM watches")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
def add_to_list(_sku,_type_watch,_status,_gender,_year,_dial_material,_dial_color,_case_material,_case_form,_bracelet_material,_movement):
    try:
        c = mydb.cursor()
        print("year type is : ", type(_year))
        s_year = str(_year)
        # We commit to save the change
        sql = "INSERT INTO watches(sku,type_watches,status,gender,year," \
                  "dial_material,dial,dial_material, dial_color, case_material," \
                  "case_form, bracelet_material, movement) VALUES(%s, set('watch', 'chrono')," \
                  " set('old', 'current', 'outlet'),enum('man', 'woman'), %s,%s,%s,%s,%s,%s,%s)"
        val = (_sku, _type_watch, _status, _gender, s_year
                    , _dial_material, _dial_color, _case_material
                    , _case_form, _bracelet_material,  _movement)
        c.execute(sql, val)
        mydb.commit()
        return {"val": val, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None
def get_all_teachers():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM teacher")
        myresult = mycursor.fetchall()
        return { "count": len(myresult), "items": myresult }
    except Exception as e:
        print('Error: ', e)
        return None


def get_watch(value):
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM watches WHERE sku=%s", value)
        myresult = mycursor.fetchall()
        return { "count": len(myresult), "items": myresult }
    except Exception as e:
        print('Error: ', e)
        return None


def get_by_pref(value):
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM watches WHERE sku LIKE %s", (value + "%"))
        myresult = mycursor.fetchall()
        return { "count": len(myresult), "items": myresult }
    except Exception as e:
        print('Error: ', e)
        return None


def generate_sql(dictionary):
    sql = '"SELECT * FROM watches WHERE'
    if len(dictionary) == 1:
        sql = '"SELECT * FROM watches WHERE ' + list(dictionary.items())[0] + '=%s"'
    # else:
    #     for item in dictionary.items():
    #         sql = sql + " " + str(item[0]) = %s"
    #     return sql


def get_by_criteria(_sku,_type_watch,_status,_gender,_year,_dial_material,_dial_color,_case_material,_case_form,_bracelet_material,_movement, dict_obj):
    print("getting by criteria")
    generate_sql(dict_obj)
    # try:
    #     mycursor = mydb.cursor()
    #    # mycursor.execute("SELECT * FROM watches WHERE sku LIKE %s", (value + "%"))
    #     myresult = mycursor.fetchall()
    #     return { "count": len(myresult), "items": myresult }
    # except Exception as e:
    #     print('Error: ', e)
    #     return None


def delete_watch(sku):
        try:
            conn = mydb
            c = conn.cursor()
            c.execute(
                "DELETE FROM watches WHERE sku = %s",
                (sku))
            conn.commit()
            return {'sku': sku}
        except Exception as e:
            print('Error: ', e)
            return None


def update_status(_sku,_type_watch,_status,_gender,_year,_dial_material,_dial_color,_case_material,_case_form,_bracelet_material,_movement):
            # Check if the passed status is a valid value
            try:
                print("trying to update")
                conn = mydb
                c = conn.cursor()
                c.execute("UPDATE watches SET type=%s,status=%s,gender=%s,year=%s,dial_material=%s,dial_color=%s,case_material=%s,case_form=%s,bracelet_material=%s,movement=%s WHERE sku=%s",(_type_watch,_status,_gender,_year,_dial_material,_dial_color,_case_material,_case_form,_bracelet_material,_movement, _sku))
                conn.commit()
                return {'sku': _sku}
            except Exception as e:
                print('Error: ', e)
                return 'Failure'