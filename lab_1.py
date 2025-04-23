from lab_4 import BinaryTree


def create_block(block_id, view, value):
    return {'id': block_id, 'view': view, 'value': value}

def can_add_to_chain(chain, block, votes):
    if block['id'] in votes and block['view'] == len(chain):
        return True
    return False

def main():
    blocks = []
    votes = set()

    while True:
        user_input = input("Введіть блок у форматі id:view:value (або 'stop' для завершення): ")
        if user_input.lower() == 'stop':
            break
        try:
            block_id, view, value = user_input.split(":")
            if any(block['id'] == block_id for block in blocks):
                print("Блок з таким id вже існує. Спробуйте ще раз.")
                continue
            block = create_block(block_id, int(view), float(value))
            blocks.append(block)
        except ValueError:
            print("Невірний формат, спробуйте ще раз.")

    while True:
        user_input = input("Введіть блок для голосування у форматі id (або 'stop' для завершення): ")
        if user_input.lower() == 'stop':
            break
        votes.add(user_input)

    chain = []
    blocks.sort(key=lambda x: x['view'])

    for block in blocks:
        if can_add_to_chain(chain, block, votes):
            chain.append(block)
            print(f"Block {block['id']} added to chain")
    
    tree = BinaryTree()
    tree.build_tree(chain)

if __name__ == "__main__":
    main()
