import pandas as pd

df = pd.read_csv('astronauts.csv')
grad_majors = pd.concat([df['Graduate Major'], df['Undergraduate Major']])

grads = []
grads_count = []
for grad in grad_majors:
    if isinstance(grad, str):
        grad = grad.split('&')
        grad = [text.strip() for text in grad]
        for txt in grad:
            if txt not in grads:
                grads.append(txt)
                grads_count.append(1)
            else:
                grads_count[grads.index(txt)] += 1

print(grads)
print(grads_count)

