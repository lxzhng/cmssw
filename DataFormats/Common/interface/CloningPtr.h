#ifndef DataFormats_Common_CloningPtr_h
#define DataFormats_Common_CloningPtr_h
// -*- C++ -*-
//
// Package:     Common
// Class  :     CloningPtr
//
/**\class CloningPtr CloningPtr.h DataFormats/Common/interface/CloningPtr.h

 Description: A smart pointer that owns its pointer and clones it when necessary

 Usage:
    <usage>

*/
//
// Original Author:  Chris Jones
//         Created:  Mon Apr  3 16:43:29 EDT 2006
//

// system include files
#include <algorithm>
#include <memory>

// user include files
#include "DataFormats/Common/interface/ClonePolicy.h"

// forward declarations
namespace edm {
  template <class T, class P = ClonePolicy<T> >
  class CloningPtr {
  public:
    CloningPtr() : ptr_(nullptr) {}
    CloningPtr(const T& iPtr) : ptr_(P::clone(iPtr)) {}
    CloningPtr(std::unique_ptr<T> iPtr) : ptr_(iPtr.release()) {}
    CloningPtr(const CloningPtr<T, P>& iPtr) : ptr_(P::clone(*(iPtr.ptr_))) {}

    CloningPtr<T, P>& operator=(const CloningPtr<T, P>& iRHS) {
      CloningPtr<T, P> temp(iRHS);
      swap(temp);
      return *this;
    }

    void swap(CloningPtr<T, P>& iPtr) { std::swap(ptr_, iPtr.ptr_); }

    ~CloningPtr() { delete ptr_; }

    // ---------- const member functions ---------------------
    T& operator*() { return *ptr_; }

    T* operator->() { return ptr_; }

    T* get() { return ptr_; }

  private:
    T* ptr_;
  };

  // Free swap function
  template <class T, class P>
  inline void swap(CloningPtr<T, P>& a, CloningPtr<T, P>& b) {
    a.swap(b);
  }
}  // namespace edm
#endif
