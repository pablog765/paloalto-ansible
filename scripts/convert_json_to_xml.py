#!/usr/bin/env python3
import json
import sys
import re

try:
    import xmltodict
except Exception as e:
    print('xmltodict no está disponible:', e, file=sys.stderr)
    sys.exit(2)


def find_key(obj, key):
    """Recorre recursivamente dicts/listas para encontrar la primera ocurrencia de `key`. devuelve el valor o None."""
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for v in obj.values():
            found = find_key(v, key)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = find_key(item, key)
            if found is not None:
                return found
    return None


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Uso: convert_json_to_xml.py input.jsonlike output.xml')
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Intentar recortar basura al final (por ejemplo un '%' extra)
    last_brace = raw.rfind('}')
    if last_brace != -1 and last_brace < len(raw) - 1:
        raw = raw[:last_brace+1]

    # También limpiar posibles caracteres iniciales no JSON
    first_brace = raw.find('{')
    if first_brace > 0:
        raw = raw[first_brace:]

    try:
        data = json.loads(raw)
    except Exception as e:
        print('Error al parsear JSON desde el archivo:', e, file=sys.stderr)
        sys.exit(3)

    # Buscar la estructura 'config' dentro del JSON
    config = find_key(data, 'config')
    if config is None:
        # Si no se encuentra, usar el propio objeto raíz
        config = data

    # Si config es una lista o contiene 'result' que tiene 'config', intenta más
    # xmltodict.unparse espera un dict con 1 root element.
    # Si config tiene múltiples keys, lo envolvemos en un root genérico si hace falta.
    if not isinstance(config, dict):
        # envolver en root
        config = {'root': config}
    else:
        # Si el dict tiene keys que no representan un único root, envolver también
        if len(config.keys()) != 1:
            config = {'root': config}

    try:
        xml = xmltodict.unparse(config, pretty=True)
    except Exception as e:
        print('Error al convertir a XML:', e, file=sys.stderr)
        sys.exit(4)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xml)

    print('XML formateado guardado en', output_path)
