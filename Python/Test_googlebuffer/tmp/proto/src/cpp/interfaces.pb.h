// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: interfaces.proto

#ifndef PROTOBUF_interfaces_2eproto__INCLUDED
#define PROTOBUF_interfaces_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2006000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
#include "common.pb.h"
// @@protoc_insertion_point(includes)

namespace interfaces {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_interfaces_2eproto();
void protobuf_AssignDesc_interfaces_2eproto();
void protobuf_ShutdownFile_interfaces_2eproto();

class interface_info_ask;
class interface_info_ans;

// ===================================================================

class interface_info_ask : public ::google::protobuf::Message {
 public:
  interface_info_ask();
  virtual ~interface_info_ask();

  interface_info_ask(const interface_info_ask& from);

  inline interface_info_ask& operator=(const interface_info_ask& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const interface_info_ask& default_instance();

  void Swap(interface_info_ask* other);

  // implements Message ----------------------------------------------

  interface_info_ask* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const interface_info_ask& from);
  void MergeFrom(const interface_info_ask& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:
  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // optional bytes uap_topic = 1;
  inline bool has_uap_topic() const;
  inline void clear_uap_topic();
  static const int kUapTopicFieldNumber = 1;
  inline const ::std::string& uap_topic() const;
  inline void set_uap_topic(const ::std::string& value);
  inline void set_uap_topic(const char* value);
  inline void set_uap_topic(const void* value, size_t size);
  inline ::std::string* mutable_uap_topic();
  inline ::std::string* release_uap_topic();
  inline void set_allocated_uap_topic(::std::string* uap_topic);

  // optional bytes json_ask = 2;
  inline bool has_json_ask() const;
  inline void clear_json_ask();
  static const int kJsonAskFieldNumber = 2;
  inline const ::std::string& json_ask() const;
  inline void set_json_ask(const ::std::string& value);
  inline void set_json_ask(const char* value);
  inline void set_json_ask(const void* value, size_t size);
  inline ::std::string* mutable_json_ask();
  inline ::std::string* release_json_ask();
  inline void set_allocated_json_ask(::std::string* json_ask);

  // @@protoc_insertion_point(class_scope:interfaces.interface_info_ask)
 private:
  inline void set_has_uap_topic();
  inline void clear_has_uap_topic();
  inline void set_has_json_ask();
  inline void clear_has_json_ask();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::std::string* uap_topic_;
  ::std::string* json_ask_;
  friend void  protobuf_AddDesc_interfaces_2eproto();
  friend void protobuf_AssignDesc_interfaces_2eproto();
  friend void protobuf_ShutdownFile_interfaces_2eproto();

  void InitAsDefaultInstance();
  static interface_info_ask* default_instance_;
};
// -------------------------------------------------------------------

class interface_info_ans : public ::google::protobuf::Message {
 public:
  interface_info_ans();
  virtual ~interface_info_ans();

  interface_info_ans(const interface_info_ans& from);

  inline interface_info_ans& operator=(const interface_info_ans& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const interface_info_ans& default_instance();

  void Swap(interface_info_ans* other);

  // implements Message ----------------------------------------------

  interface_info_ans* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const interface_info_ans& from);
  void MergeFrom(const interface_info_ans& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:
  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // optional bytes json_ans = 1;
  inline bool has_json_ans() const;
  inline void clear_json_ans();
  static const int kJsonAnsFieldNumber = 1;
  inline const ::std::string& json_ans() const;
  inline void set_json_ans(const ::std::string& value);
  inline void set_json_ans(const char* value);
  inline void set_json_ans(const void* value, size_t size);
  inline ::std::string* mutable_json_ans();
  inline ::std::string* release_json_ans();
  inline void set_allocated_json_ans(::std::string* json_ans);

  // optional .common.errorinfo error = 2;
  inline bool has_error() const;
  inline void clear_error();
  static const int kErrorFieldNumber = 2;
  inline const ::common::errorinfo& error() const;
  inline ::common::errorinfo* mutable_error();
  inline ::common::errorinfo* release_error();
  inline void set_allocated_error(::common::errorinfo* error);

  // @@protoc_insertion_point(class_scope:interfaces.interface_info_ans)
 private:
  inline void set_has_json_ans();
  inline void clear_has_json_ans();
  inline void set_has_error();
  inline void clear_has_error();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::std::string* json_ans_;
  ::common::errorinfo* error_;
  friend void  protobuf_AddDesc_interfaces_2eproto();
  friend void protobuf_AssignDesc_interfaces_2eproto();
  friend void protobuf_ShutdownFile_interfaces_2eproto();

  void InitAsDefaultInstance();
  static interface_info_ans* default_instance_;
};
// ===================================================================


// ===================================================================

// interface_info_ask

// optional bytes uap_topic = 1;
inline bool interface_info_ask::has_uap_topic() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void interface_info_ask::set_has_uap_topic() {
  _has_bits_[0] |= 0x00000001u;
}
inline void interface_info_ask::clear_has_uap_topic() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void interface_info_ask::clear_uap_topic() {
  if (uap_topic_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    uap_topic_->clear();
  }
  clear_has_uap_topic();
}
inline const ::std::string& interface_info_ask::uap_topic() const {
  // @@protoc_insertion_point(field_get:interfaces.interface_info_ask.uap_topic)
  return *uap_topic_;
}
inline void interface_info_ask::set_uap_topic(const ::std::string& value) {
  set_has_uap_topic();
  if (uap_topic_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    uap_topic_ = new ::std::string;
  }
  uap_topic_->assign(value);
  // @@protoc_insertion_point(field_set:interfaces.interface_info_ask.uap_topic)
}
inline void interface_info_ask::set_uap_topic(const char* value) {
  set_has_uap_topic();
  if (uap_topic_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    uap_topic_ = new ::std::string;
  }
  uap_topic_->assign(value);
  // @@protoc_insertion_point(field_set_char:interfaces.interface_info_ask.uap_topic)
}
inline void interface_info_ask::set_uap_topic(const void* value, size_t size) {
  set_has_uap_topic();
  if (uap_topic_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    uap_topic_ = new ::std::string;
  }
  uap_topic_->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:interfaces.interface_info_ask.uap_topic)
}
inline ::std::string* interface_info_ask::mutable_uap_topic() {
  set_has_uap_topic();
  if (uap_topic_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    uap_topic_ = new ::std::string;
  }
  // @@protoc_insertion_point(field_mutable:interfaces.interface_info_ask.uap_topic)
  return uap_topic_;
}
inline ::std::string* interface_info_ask::release_uap_topic() {
  clear_has_uap_topic();
  if (uap_topic_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    return NULL;
  } else {
    ::std::string* temp = uap_topic_;
    uap_topic_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    return temp;
  }
}
inline void interface_info_ask::set_allocated_uap_topic(::std::string* uap_topic) {
  if (uap_topic_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    delete uap_topic_;
  }
  if (uap_topic) {
    set_has_uap_topic();
    uap_topic_ = uap_topic;
  } else {
    clear_has_uap_topic();
    uap_topic_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  // @@protoc_insertion_point(field_set_allocated:interfaces.interface_info_ask.uap_topic)
}

// optional bytes json_ask = 2;
inline bool interface_info_ask::has_json_ask() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void interface_info_ask::set_has_json_ask() {
  _has_bits_[0] |= 0x00000002u;
}
inline void interface_info_ask::clear_has_json_ask() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void interface_info_ask::clear_json_ask() {
  if (json_ask_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ask_->clear();
  }
  clear_has_json_ask();
}
inline const ::std::string& interface_info_ask::json_ask() const {
  // @@protoc_insertion_point(field_get:interfaces.interface_info_ask.json_ask)
  return *json_ask_;
}
inline void interface_info_ask::set_json_ask(const ::std::string& value) {
  set_has_json_ask();
  if (json_ask_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ask_ = new ::std::string;
  }
  json_ask_->assign(value);
  // @@protoc_insertion_point(field_set:interfaces.interface_info_ask.json_ask)
}
inline void interface_info_ask::set_json_ask(const char* value) {
  set_has_json_ask();
  if (json_ask_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ask_ = new ::std::string;
  }
  json_ask_->assign(value);
  // @@protoc_insertion_point(field_set_char:interfaces.interface_info_ask.json_ask)
}
inline void interface_info_ask::set_json_ask(const void* value, size_t size) {
  set_has_json_ask();
  if (json_ask_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ask_ = new ::std::string;
  }
  json_ask_->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:interfaces.interface_info_ask.json_ask)
}
inline ::std::string* interface_info_ask::mutable_json_ask() {
  set_has_json_ask();
  if (json_ask_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ask_ = new ::std::string;
  }
  // @@protoc_insertion_point(field_mutable:interfaces.interface_info_ask.json_ask)
  return json_ask_;
}
inline ::std::string* interface_info_ask::release_json_ask() {
  clear_has_json_ask();
  if (json_ask_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    return NULL;
  } else {
    ::std::string* temp = json_ask_;
    json_ask_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    return temp;
  }
}
inline void interface_info_ask::set_allocated_json_ask(::std::string* json_ask) {
  if (json_ask_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    delete json_ask_;
  }
  if (json_ask) {
    set_has_json_ask();
    json_ask_ = json_ask;
  } else {
    clear_has_json_ask();
    json_ask_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  // @@protoc_insertion_point(field_set_allocated:interfaces.interface_info_ask.json_ask)
}

// -------------------------------------------------------------------

// interface_info_ans

// optional bytes json_ans = 1;
inline bool interface_info_ans::has_json_ans() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void interface_info_ans::set_has_json_ans() {
  _has_bits_[0] |= 0x00000001u;
}
inline void interface_info_ans::clear_has_json_ans() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void interface_info_ans::clear_json_ans() {
  if (json_ans_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ans_->clear();
  }
  clear_has_json_ans();
}
inline const ::std::string& interface_info_ans::json_ans() const {
  // @@protoc_insertion_point(field_get:interfaces.interface_info_ans.json_ans)
  return *json_ans_;
}
inline void interface_info_ans::set_json_ans(const ::std::string& value) {
  set_has_json_ans();
  if (json_ans_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ans_ = new ::std::string;
  }
  json_ans_->assign(value);
  // @@protoc_insertion_point(field_set:interfaces.interface_info_ans.json_ans)
}
inline void interface_info_ans::set_json_ans(const char* value) {
  set_has_json_ans();
  if (json_ans_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ans_ = new ::std::string;
  }
  json_ans_->assign(value);
  // @@protoc_insertion_point(field_set_char:interfaces.interface_info_ans.json_ans)
}
inline void interface_info_ans::set_json_ans(const void* value, size_t size) {
  set_has_json_ans();
  if (json_ans_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ans_ = new ::std::string;
  }
  json_ans_->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:interfaces.interface_info_ans.json_ans)
}
inline ::std::string* interface_info_ans::mutable_json_ans() {
  set_has_json_ans();
  if (json_ans_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    json_ans_ = new ::std::string;
  }
  // @@protoc_insertion_point(field_mutable:interfaces.interface_info_ans.json_ans)
  return json_ans_;
}
inline ::std::string* interface_info_ans::release_json_ans() {
  clear_has_json_ans();
  if (json_ans_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    return NULL;
  } else {
    ::std::string* temp = json_ans_;
    json_ans_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    return temp;
  }
}
inline void interface_info_ans::set_allocated_json_ans(::std::string* json_ans) {
  if (json_ans_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    delete json_ans_;
  }
  if (json_ans) {
    set_has_json_ans();
    json_ans_ = json_ans;
  } else {
    clear_has_json_ans();
    json_ans_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  // @@protoc_insertion_point(field_set_allocated:interfaces.interface_info_ans.json_ans)
}

// optional .common.errorinfo error = 2;
inline bool interface_info_ans::has_error() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void interface_info_ans::set_has_error() {
  _has_bits_[0] |= 0x00000002u;
}
inline void interface_info_ans::clear_has_error() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void interface_info_ans::clear_error() {
  if (error_ != NULL) error_->::common::errorinfo::Clear();
  clear_has_error();
}
inline const ::common::errorinfo& interface_info_ans::error() const {
  // @@protoc_insertion_point(field_get:interfaces.interface_info_ans.error)
  return error_ != NULL ? *error_ : *default_instance_->error_;
}
inline ::common::errorinfo* interface_info_ans::mutable_error() {
  set_has_error();
  if (error_ == NULL) error_ = new ::common::errorinfo;
  // @@protoc_insertion_point(field_mutable:interfaces.interface_info_ans.error)
  return error_;
}
inline ::common::errorinfo* interface_info_ans::release_error() {
  clear_has_error();
  ::common::errorinfo* temp = error_;
  error_ = NULL;
  return temp;
}
inline void interface_info_ans::set_allocated_error(::common::errorinfo* error) {
  delete error_;
  error_ = error;
  if (error) {
    set_has_error();
  } else {
    clear_has_error();
  }
  // @@protoc_insertion_point(field_set_allocated:interfaces.interface_info_ans.error)
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace interfaces

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_interfaces_2eproto__INCLUDED
