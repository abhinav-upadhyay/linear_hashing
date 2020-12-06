# Copyright (c) 2020,2021, Abhinav Upadhyay
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import time
import hashmap

NRECORDS = 10 ** 6

def main():
    print("pid: %d", os.getpid())
    linear_hashmap_test()
    hashmap_test()
    hashmap_test_nogrow()

def hashmap_test_nogrow():
    nrecords = NRECORDS
    keys = ["k%d" % i for i in range(nrecords)]
    vals = ["v%d" % i for i in range(nrecords)]
    start = time.time()
    m = hashmap.HashMap(grow=False)
    for i in range(nrecords):
        m.put(keys[i], vals[i])
    for i in range(nrecords):
        v = m.get(keys[i])
        assert v == vals[i], "Expected value %s for key %s, got %s" % (vals[i], keys[i], v)
    end = time.time()
    print("Time taken for linear probing hash table impl without growing for %d enties: %f seconds" % (nrecords, end - start))


def hashmap_test():
    nrecords = NRECORDS
    keys = ["k%d" % i for i in range(nrecords)]
    vals = ["v%d" % i for i in range(nrecords)]
    start = time.time()
    m = hashmap.HashMap()
    for i in range(nrecords):
        m.put(keys[i], vals[i])
    for i in range(nrecords):
        v = m.get(keys[i])
        assert v == vals[i], "Expected value %s for key %s, got %s" % (vals[i], keys[i], v)
    end = time.time()
    print("Time taken for linear probing hash table impl for %d enties: %f seconds" % (nrecords, end - start))

def linear_hashmap_test():
    nrecords = NRECORDS
    keys = ["k%d" % i for i in range(nrecords)]
    vals = ["v%d" % i for i in range(nrecords)]
    start = time.time()
    m = hashmap.LinearHashMap()
    for i in range(nrecords):
        m.put(keys[i], vals[i])
    for i in range(nrecords):
        v = m.get(keys[i])
        assert v == vals[i], "Expected value %s for key %s, got %s" % (vals[i], keys[i], v)
    end = time.time()
    print("Time taken for linear hash table impl for %d enties: %f seconds" % (nrecords, end - start))


if __name__ == '__main__':
    main()
