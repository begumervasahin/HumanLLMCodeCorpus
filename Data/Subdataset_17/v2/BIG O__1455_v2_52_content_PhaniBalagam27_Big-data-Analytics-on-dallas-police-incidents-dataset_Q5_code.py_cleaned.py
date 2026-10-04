from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from subprocess import call
def main():
    conf = SparkConf().setAppName("Q2")
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)
    csv_path = 'pxb161930/Police_Incidents.csv'
    df = sqlContext.read.load(csv_path, format='csv', header='true', inferSchema='true')
    excluded_columns = [
        'Incident Number w/ Year', 'Watch', 'Call (911) Problem', 'Type of Incident', 'Penalty Class', 'Type of Location',
        'Type of Property', 'Street Block', 'Street Direction', 'Street Name', 'Incident Address', 'City', 'X Coordinate',
        'Y Coordinate', 'Reporting Area', 'Beat', 'Division', 'Sector', 'Council District', 'Target Area Action Grids',
        'Community','Ending Date/Time', 'Map Date', 'Date of Report', 'Date incident created', 'Offense Entered Time',
        'Offense Entered  Date/Time', 'Call Date Time','Call Dispatch Date Time', 'Complainant Age',
        'Complainant Age at Offense', 'Complainant Home Address', 'Complainant Zip Code', 'Complainant City',
        'Complainant Business Name', 'Complainant Business Address', 'Investigating Unit 1', 'Investigating Unit 2',
        'Offense Status', 'Victim Injury Description', 'Victim Condition', 'RMS Code', 'Offense Code CC', 'CJIS Code',
        'Penal Code', 'UCR Offense Name', 'Modus Operandi (MO)', 'Hate Crime', 'Gang Related Offense', 'Drug Related Incident'
    ]
    selected_columns = [col for col in df.columns if col not in excluded_columns]
    df_selected = df.select(selected_columns)
    df_cleaned = df_selected.toDF(*(c.replace(' ', '_').replace('/', '').replace('(', '').replace(')', '').replace('__', '_') for c in df_selected.columns))
    df_cleaned.registerTempTable("q5data")
    sqlContext.sql("DROP TABLE IF EXISTS default.q5table")
    sqlContext.sql("CREATE TABLE default.q5table AS SELECT * FROM q5data")
    hive_query = "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM default.q5table"
    call(["hive", "-e", hive_query])
    sc.stop()
if __name__ == '__main__':
    main()