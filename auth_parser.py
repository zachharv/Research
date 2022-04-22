#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def dict_parser(file):
  nums=['1','2','3','4','5','6','7','8','9','0']
  findingip=0
  result={}
  workingip=''
  checker=0
  for line in file:
    if 'ssh' in line:
      findingip=0
      checker=0
      for char in line.rstrip():
        if char in nums:
          workingip+=char
          findingip+=1
        if char=='.':
          workingip+=char
          findingip+=10
        if char==' ' and findingip>33:
          if workingip in result:
            result[workingip]+=1
          else:
            result[workingip]=1
          checker=1
        if char not in nums and char!='.':
          findingip=0
          workingip=''
      if checker==0 and findingip>33:
        if workingip in result:
          result[workingip]+=1
        else:
          result[workingip]=1
      workingip=''
      findingip=0
  return result

def auth_parser(dict):
  iplog=dict
  del iplog['0.0.0.0']
  total=0
  tuplegrabber=()
  result='-------------------------------------\n| Percent | Count |              IP |\n-------------------------------------\n'
  for value in iplog.values():
    total+=value
  for k in sorted(iplog, key=iplog.get):
    tuplegrabber=((k, iplog[k]))
    percent=str(tuplegrabber[1]/total*100)
    if len(percent)>6:
      percent=percent[0:6]
    if len(percent)<6:
      percent=percent+(6-len(percent))*'0'
    count=str(tuplegrabber[1])
    ip=str(tuplegrabber[0])
    result+='|  '+percent+' |'
    result+=(' '*(6-len(count))) +count+ ' |'
    result+=(' '*(16-len(ip))) +ip+ ' |\n'
  total=str(total)
  result+='-------------------------------------\n'
  result+='|   Total |'
  result+=(' '*(6-len(total))) +total+ ' |'
  result+=(' '*17) +'|\n'
  result+='-------------------------------------'
    
  print(result)

### MAIN FUNCTION ###
formed_dict={}
def main():
  file_name=sys.argv[1]
  open_file=open(file_name)
  formed_dict=dict_parser(open_file)
  open_file.close()
  auth_parser(formed_dict)

  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
