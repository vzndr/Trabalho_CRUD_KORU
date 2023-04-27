from flask import Flask, jsonify, request

app = Flask(__name__)

products = {
      0:{
        "id": "0",
        "nome": "Echo Dot 4a Geracao",
        "preco":"379,05",
        "peso": "328g",
        "descricao": "Musica, informacao e Casa Inteligente - Cor Preta",
        "fornecedor": "Amazon"
        }
}

# função para criar um produto a a partir de requisição post em json
def create_product():
    body = request.json
    id = generate_id()
    products[id] = {
        'id': id,
        'nome': request.json["nome"],
        'preco': request.json["preco"],
        'peso': request.json["peso"],
        'descricao': request.json["descricao"],
        'fornecedor': request.json["fornecedor"]
    }
    return jsonify(products)

# função para gerar id de cada produto
def generate_id():
    id = max(products.keys()) + 1
    return id

#Página inicial
@app.route('/', methods=['GET'])
def home_page():
    return 'Ok.'

#Mostra todos os produtos
@app.route('/products', methods=['GET'])
def show_all_products():
    return jsonify(products)

#Busca e mostra produto especifício
@app.route('/product/<int:id>', methods=['GET'])
def get_specific_product(id:int):
    for product in products:
        if product == id: 
            body = products[id]
            return jsonify(body)
    return jsonify({"message": "Este produto não existe no momento."})

#Exclui um produto
@app.route('/<int:id>', methods=['DELETE'])
def remove_product_by_id(id):
    for product in products:
        if product['id'] == id:
            products.pop(product)
            return jsonify({'message': 'Produto removido.'})
    return jsonify({'message': 'O produto que você está tentando remover não existe. Verifique o código e tente novamente.'})

#Atualiza um produto
@app.route('/product/<int:id>', methods=['PUT' , 'DELETE'])
def update_product_by_id(id:int):
    if request.method == "PUT":
        for chave, dinossauro in products.items():
            if chave == id:
                products[id] = {
                                            'id': id,
                                            'nome': request.json["nome"],
                                            'preco': request.json["preco"],
                                            'peso': request.json["peso"],
                                            'descricao': request.json["descricao"],
                                            'fornecedor': request.json["fornecedor"]
                                          }
                return jsonify(products[id])
        return jsonify({'message': "O produto que você está tentando alterar não existe. Verifique o código e tente novamente."})

    else:
        for chave, dinossauro in products.items():
            if chave == id:
                body = products[id]
                products.pop(chave)
                return jsonify("Produto removido com sucesso.", body)
        return jsonify({'message': "O produto que você está tentando remover não existe. Verifique o código e tente novamente."})



# Criar rota para adicionar um novo produto
@app.route('/product', methods=['POST'])
def add_product():
   body = create_product()
   return body


app.run(debug=True)

