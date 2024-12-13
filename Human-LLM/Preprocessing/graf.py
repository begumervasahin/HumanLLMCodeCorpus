import ast
import networkx as nx
import os
import multiprocessing
import matplotlib.pyplot as plt
import numpy as np

# AST'den renkli görüntü oluşturmak için renkler
colors = {
    "Module": (255, 255, 255),  # Beyaz
    "FunctionDef": (255, 0, 0),  # Kırmızı
    "Assign": (0, 255, 0),  # Yeşil
    "Call": (0, 0, 255),  # Mavi
    # İhtiyaca göre AST'deki diğer düğümler için renkler eklenebilir
}

def generate_ast(code):
    """
    Python kodunu AST'ye dönüştürür.
    """
    try:
        tree = ast.parse(code)
        return tree
    except SyntaxError as e:
        print(f"SyntaxError occurred while parsing the code: {e}")
        return None

def ast_to_image(ast_tree, output_file_path):
    """
    AST'yi renkli bir görüntü olarak temsil eder ve dosyaya kaydeder.
    """
    graph = nx.DiGraph()

    def visit(node, parent=None):
        """
        AST'yi dolaşarak grafı oluşturur.
        """
        graph.add_node(node)
        if parent is not None:
            graph.add_edge(parent, node)

        for child in ast.iter_child_nodes(node):
            visit(child, node)

    visit(ast_tree)

    pos = nx.spring_layout(graph)  # Düğümleri otomatik olarak düzenleme

    # Görüntüyü oluşturma
    fig, ax = plt.subplots(figsize=(16, 16))  # Görüntü boyutunu ayarlama
    ax.set_axis_off()
    ax.set_aspect(1)
    
    for node in graph.nodes:
        node_type = type(node).__name__
        color = colors.get(node_type, (128, 128, 128))  # Bilinmeyen düğümler için gri renk
        nx.draw_networkx_nodes(graph, pos, nodelist=[node], node_color=[np.array(color) / 255], node_shape='s', ax=ax)
        nx.draw_networkx_labels(graph, pos, labels={node: node_type}, font_color='black', font_size=3, ax=ax)

    for edge in graph.edges:
        nx.draw_networkx_edges(graph, pos, edgelist=[edge], edge_color='black', ax=ax)

    plt.savefig(output_file_path, format='png')  # Görüntüyü kaydet
    plt.close()

def process_file(file_path, output_directory):
    """
    Bir Python dosyası için AST oluşturur ve görüntüye dönüştürür.
    """
    with open(file_path, "r", encoding="utf-8") as code_file:
        code = code_file.read()

    ast_tree = generate_ast(code)
    if ast_tree is not None:
        output_file_path = os.path.join(output_directory, f"{os.path.splitext(os.path.basename(file_path))[0]}.png")
        ast_to_image(ast_tree, output_file_path)
        print(f"AST image created and saved for file: {file_path}")

def main():
    input_directory = r"C:\Users\ervas\OneDrive\Masaüstü\Bitirme ap\veri temizleme\Zararsız4o_cleaned_codes"
    
    output_directory = r"C:\Users\ervas\OneDrive\Masaüstü\Bitirme ap\veri temizleme\4o_zararsız_graf"
    os.makedirs(output_directory, exist_ok=True)

    pool = multiprocessing.Pool()  # Multiprocessing havuzu oluştur

    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                pool.apply_async(process_file, args=(file_path, output_directory))  # Dosyaları paralel işleme gönder

    pool.close()
    pool.join()  # İşlemleri tamamlamayı bekleyin

if __name__ == "__main__":
    main()
