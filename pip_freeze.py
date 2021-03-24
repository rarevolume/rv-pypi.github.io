import subprocess
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
req_file = os.path.join(dir_path, 'requirements.txt')
libs = ['rv-transcode', 'rv-scms']
extra_url = '--extra-index-url https://rarevolume.github.io/rv-pypi.github.io/\n'

# call pip freeze
with open(req_file, 'w') as f:
  process = subprocess.Popen(['pip', 'freeze'], stdout=f, stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  print(stdout)
  print(stderr)

# open requirements.txt and stored original lines
with open(req_file, 'r') as f:
  req = f.readlines()

# add --extra-index-url
new_req = []
for i, line in enumerate(req):
  for l in libs:
    if line.startswith(l):
      new_req.append(extra_url)
      break
  new_req.append(line)

# write to file
with open(req_file, 'w') as f:
  f.writelines(new_req)

# print new requirements
with open(req_file, 'r') as f:
  print(f.read())
