import requests

url = "http://activist-birds.picoctf.net:50469"

test_cases = [
    (0, 4),
    (1, 5),
    (100, 104),
    (0x100, 0x104),
    (0x1000, 0x1004),
]

for inp_start, out_start in test_cases:
    circuit = []
    
    for i in range(4):
        circuit.append({
            "input1": inp_start + i,
            "input2": inp_start + i,
            "output": out_start + i
        })
    
    print(f"\nTrying: inputs={inp_start}-{inp_start+3}, outputs={out_start}-{out_start+3}")
    
    try:
        res = requests.post(f'{url}/check', json={"circuit": circuit})
        if res.status_code == 200:
            result = res.json()
            print(f"Result: {result['flag']}")
    except Exception as e:
        print(f"Error: {e}")