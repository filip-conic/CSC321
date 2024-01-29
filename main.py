import hashlib
import time

word_count = 466549
words_digest = {}

#digest size in bits
def hash_with_shortened_digest(input_string, digest_size):
    hasher = hashlib.sha256()
    hasher.update(input_string.encode())
    hex_digest = hasher.hexdigest()
    binary_digest = bin(int(hex_digest, 16))
    return binary_digest[2:digest_size+2]

def find_collision_digest_length(digest_length, words):
    print("Finding collision for digest size of " + str(digest_length))
    start_time = time.perf_counter()
    found_collision = False

    for i in range(word_count):
        w1 = words[i].strip()
        w1_dig = words_digest[w1][:digest_length]

        for j in range(i+1, word_count):
            w2 = words[j].strip()
            if w1 == w2 or w1 == "" or w2 == "":
                continue

            w2_dig = words_digest[w2][:digest_length]

            if(w1_dig == w2_dig):
                found_collision = True
                break

        if found_collision:
            time_elapsed = time.perf_counter() - start_time
            print("Found Collision!")
            print("Word 1: \"" + w1 + "\", Word 2: \"" + w2 + "\"")
            print("Word 1 Digest: " + w1_dig + ", Word 2 Digest: " + w2_dig)
            print("Time Elapsed: " + str(time_elapsed) + "\n")
            break

    if not found_collision:
        print("No collision was found")

def create_digest_dict(words):
    for i in range(word_count):
        word = words[i].strip()
        word_digest = hash_with_shortened_digest(word, 50)
        words_digest[word] = word_digest

def main():


    # for i in range(len(words)):
    #     word = words[i].strip()
    #     print(word)
    #     if i > 50:
    #         time.sleep(1)

    f = open("words.txt")
    words = f.readlines();
    f.close()

    create_digest_dict(words)


    for i in range(2, 50, 2):
        find_collision_digest_length(i, words)


if __name__ == '__main__':
    main()