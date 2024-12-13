from flask import Flask, request, jsonify
import graphene

# Define your schema here (assuming it's already done)
# Example schema for demonstration:
class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello, World!"

schema = graphene.Schema(query=Query)

app = Flask(__name__)

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request. Must provide a valid GraphQL query."}), 400

    result = schema.execute(
        data.get('query'),
        variable_values=data.get('variables'),
        context_value=request
    )
    
    # Check if result has errors
    if result.errors:
        return jsonify({"errors": [str(error) for error in result.errors]})
    
    # Ensure result.data is not None
    return jsonify(result.data or {})


if __name__ == '__main__':
    app.run(debug=True)
