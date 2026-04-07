import json

with open('MULTI_DISEASE_PREDICTION_SYSTEM.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('retrain_models.py', 'w', encoding='utf-8') as out:
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            out.write(source)
            out.write('\n\n')
