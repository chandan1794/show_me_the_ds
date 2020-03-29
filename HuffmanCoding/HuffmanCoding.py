import sys
import heapq


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if other is None:
            return -1
        if not isinstance(other, HuffmanNode):
            return -1
        return self.freq < other.freq

    def __repr__(self):
        return f"{self.char}: {self.freq}"


class HuffmanTree:
    def __init__(self, data):
        self.data: str = data
        self.tree = []
        self.codes = {}
        self.reverse_mapping = {}

    def encode_data(self):
        # Time Complexity: O(nlogn)
        frequency = self.get_sorted_frequency()

        # Time Complexity: O(nlogn)
        self.build_heap(frequency)

        # Time Complexity: O(n)
        self.merge_frequencies()

        # Time Complexity: O(n)
        self.create_codes()

        # Time Complexity: O(n)
        return self.generate_encoded_data()

    def get_sorted_frequency(self):
        data = str(self.data)
        freq = {}

        for char in data:
            freq[char] = 1 + int(char in freq.keys())

        sorted_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}
        return sorted_freq

    def build_heap(self, frequency):
        for char in frequency:
            node = HuffmanNode(char, frequency[char])
            heapq.heappush(self.tree, node)

    def merge_frequencies(self):
        while len(self.tree) > 1:
            node_left = heapq.heappop(self.tree)
            node_right = heapq.heappop(self.tree)

            merged = HuffmanNode(None, node_left.freq + node_right.freq)
            merged.left = node_left
            merged.right = node_right

            heapq.heappush(self.tree, merged)

    def create_codes(self):
        root_node = heapq.heappop(self.tree)
        curr_code = ""
        self.helper_create_code(root_node, curr_code)

    def helper_create_code(self, root_node, curr_code):
        if root_node is None:
            return

        if root_node.char is not None:
            self.codes[root_node.char] = curr_code
            self.reverse_mapping[curr_code] = root_node.char
            return

        self.helper_create_code(root_node.left, curr_code + "0")
        self.helper_create_code(root_node.right, curr_code + "1")

    def generate_encoded_data(self):
        encoded_data = ""
        for char in self.data:
            encoded_data += self.codes[char]
        return encoded_data

    def generate_decoded_data(self, _encoded_data):
        curr_code = ""
        _decoded_data = ""

        for bit in _encoded_data:
            curr_code += bit
            if curr_code in self.reverse_mapping:
                char = self.reverse_mapping[curr_code]
                _decoded_data += char
                curr_code = ""

        return _decoded_data

    def decode_data(self, _encoded_data):
        # Time Complexity: O(n)
        return self.generate_decoded_data(_encoded_data)


def huffman_encoding(data):
    if isinstance(data, str):
        huffman_tree = HuffmanTree(data)
        return huffman_tree.encode_data(), huffman_tree
    else:
        return ""


def huffman_decoding(data, tree):
    return tree.decode_data(data)


if __name__ == "__main__":
    print(f"\n{'#' * 10} Test #1 {'#' * 10} ")
    # Test #1: True Compression happens
    sample_string = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(sample_string)))
    # The size of the data is: 69
    encoded_data, tree = huffman_encoding(sample_string)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print(f"decoded_data == original_data = {sample_string == decoded_data}")
    # decoded_data == original_data = True

    print(f"\n{'#' * 10} Test #2 {'#' * 10} ")
    # Test #2: Too Long String

    sample_string = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Why do we use it? It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
    """

    print("The size of the data is: {}\n".format(sys.getsizeof(sample_string)))
    # The size of the data is: 1265
    encoded_data, tree = huffman_encoding(sample_string)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 896

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 1265
    print(f"decoded_data == original_data = {sample_string == decoded_data}")
    # decoded_data == original_data = True

    print(f"\n{'#' * 10} Test #3 {'#' * 10} ")
    # Test #3: None

    sample_string = None
    print(huffman_encoding(sample_string))
    # Output: Empty String
    # Because cannot compress None
