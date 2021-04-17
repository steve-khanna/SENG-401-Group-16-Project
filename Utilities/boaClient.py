import time

from boaapi.boa_client import BoaClient, BOA_API_ENDPOINT

from getpass import getpass



dataSet = '2019 October/GitHub'

# query = """p: Project = input;
# counts: output collection[string] of string;
# classes: output collection[string] of int;

# exists(i: int; lowercase(input.programming_languages[i]) == "java") {
#     visit(input, visitor {
#         before node: CodeRepository -> {
#             classCounts := 0;
#             snapshot := getsnapshot(node, "SOURCE_JAVA_JLS");


#             foreach (k: int; def(snapshot[k]))
#                 classCounts++;

#             if (classCounts > 100 && classCounts < 200)
#                 classes[p.name] << classCounts;
#             stop;
#         }
#     });
# }"""


query = """p: Project = input;
counts: output collection[string] of string;
visit(input, visitor {
    before n: ASTRoot -> {
        exists (i: int; strfind(`tensorflow`, n.imports[i]) > -1)
            counts[p.id] << p.name;
    }
});"""



client = BoaClient(endpoint=BOA_API_ENDPOINT)


def init(client):

    try:
        username = input("Please enter your boa username: ")
        password = getpass("Please enter your boa password: ")

        client.login(username, password)
        print('successfully logged in to Boa API')

        runQuery(query, client)

    except:
        print("Login failed. Exiting.....\n")




def runQuery(query, client):

    # query using a specific dataset
    job = client.query(query, client.get_dataset(dataSet))
    print('query submitted')

    while job.is_running():
        job.refresh()
        #print('job ' + str(job.id) + ' still running, waiting 10s...')
        time.sleep(10)

    if job.compiler_status == 'Error':
        print('job ' + str(job.id) + ' had compile error')
    elif job.exec_status == 'Error':
        print('job ' + str(job.id) + ' had exec error')
    else:
        try:
            output = job.output().decode('utf-8')
            
            

            #print output to csv file labeled with job id.
            
            output = output.replace(" ", ",")
            output = output.replace("[", "")
            output = output.replace("classes", "")
            output = output.replace("counts", "")
            output = output.replace("]", "")
            output = outputCleanUp(output)

            writeToFile(output, job.id)

        except:
            pass

    client.close()
    print('client closed')

def writeToFile(output, id):
    filename = str(id)+".csv"
    f = open(filename, "a")
    f.write(output)
    f.close()
    
    lines_seen = set() # holds lines already seen
    with open("Output_file.csv", "w") as output_file:
        for each_line in open(filename, "r"):
            if each_line not in lines_seen: # check if line is not duplicate
                output_file.write(each_line)
                lines_seen.add(each_line)
    print("File Writing complete")




def outputCleanUp(output):
      clean = output.split('\n',)[0]
      counter = clean.count(',')

      firstStr = ""
      for i in range(counter):
          print("Working on it")
          firstStr = firstStr+ "Col"+ str(i)+ ","

      firstStr = firstStr +"Col"+str(counter)
      output = firstStr+"\n"+output
      return output


def main():
    init(client)

if __name__ == "__main__":
    main()