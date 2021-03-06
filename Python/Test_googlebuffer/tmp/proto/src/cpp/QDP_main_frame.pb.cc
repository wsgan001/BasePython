// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: QDP_main_frame.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "QDP_main_frame.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/once.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)

namespace QDP_main_frame {

namespace {

const ::google::protobuf::Descriptor* user_verification_ask_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  user_verification_ask_reflection_ = NULL;
const ::google::protobuf::Descriptor* user_verification_ans_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  user_verification_ans_reflection_ = NULL;
const ::google::protobuf::EnumDescriptor* other_platform_descriptor_ = NULL;

}  // namespace


void protobuf_AssignDesc_QDP_5fmain_5fframe_2eproto() {
  protobuf_AddDesc_QDP_5fmain_5fframe_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "QDP_main_frame.proto");
  GOOGLE_CHECK(file != NULL);
  user_verification_ask_descriptor_ = file->message_type(0);
  static const int user_verification_ask_offsets_[5] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ask, info_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ask, platform_type_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ask, ask_header_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ask, service_manager_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ask, query_type_),
  };
  user_verification_ask_reflection_ =
    new ::google::protobuf::internal::GeneratedMessageReflection(
      user_verification_ask_descriptor_,
      user_verification_ask::default_instance_,
      user_verification_ask_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ask, _has_bits_[0]),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ask, _unknown_fields_),
      -1,
      ::google::protobuf::DescriptorPool::generated_pool(),
      ::google::protobuf::MessageFactory::generated_factory(),
      sizeof(user_verification_ask));
  user_verification_ans_descriptor_ = file->message_type(1);
  static const int user_verification_ans_offsets_[3] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ans, platform_type_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ans, json_ans_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ans, error_),
  };
  user_verification_ans_reflection_ =
    new ::google::protobuf::internal::GeneratedMessageReflection(
      user_verification_ans_descriptor_,
      user_verification_ans::default_instance_,
      user_verification_ans_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ans, _has_bits_[0]),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(user_verification_ans, _unknown_fields_),
      -1,
      ::google::protobuf::DescriptorPool::generated_pool(),
      ::google::protobuf::MessageFactory::generated_factory(),
      sizeof(user_verification_ans));
  other_platform_descriptor_ = file->enum_type(0);
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_QDP_5fmain_5fframe_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
    user_verification_ask_descriptor_, &user_verification_ask::default_instance());
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
    user_verification_ans_descriptor_, &user_verification_ans::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_QDP_5fmain_5fframe_2eproto() {
  delete user_verification_ask::default_instance_;
  delete user_verification_ask_reflection_;
  delete user_verification_ans::default_instance_;
  delete user_verification_ans_reflection_;
}

void protobuf_AddDesc_QDP_5fmain_5fframe_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::QDP_basic_info::protobuf_AddDesc_QDP_5fbasic_5finfo_2eproto();
  ::common::protobuf_AddDesc_common_2eproto();
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\024QDP_main_frame.proto\022\016QDP_main_frame\032\024"
    "QDP_basic_info.proto\032\014common.proto\"\375\001\n\025u"
    "ser_verification_ask\022-\n\004info\030\001 \001(\0132\037.QDP"
    "_basic_info.user_basic_info\0225\n\rplatform_"
    "type\030\002 \001(\0162\036.QDP_main_frame.other_platfo"
    "rm\022-\n\nask_header\030\003 \001(\0132\031.common.common_a"
    "sk_header\0228\n\017service_manager\030\004 \001(\0132\037.QDP"
    "_basic_info.control_service\022\025\n\nquery_typ"
    "e\030\005 \001(\005:\0010\"\202\001\n\025user_verification_ans\0225\n\r"
    "platform_type\030\001 \001(\0162\036.QDP_main_frame.oth"
    "er_platform\022\020\n\010json_ans\030\002 \001(\014\022 \n\005error\030\003"
    " \001(\0132\021.common.errorinfo*`\n\016other_platfor"
    "m\022\024\n\020unknown_platform\020\000\022\021\n\rCredit_sesame"
    "\020\001\022\020\n\014fraud_metrix\020\002\022\023\n\017AnRong_Platform\020"
    "\003", 561);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "QDP_main_frame.proto", &protobuf_RegisterTypes);
  user_verification_ask::default_instance_ = new user_verification_ask();
  user_verification_ans::default_instance_ = new user_verification_ans();
  user_verification_ask::default_instance_->InitAsDefaultInstance();
  user_verification_ans::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_QDP_5fmain_5fframe_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_QDP_5fmain_5fframe_2eproto {
  StaticDescriptorInitializer_QDP_5fmain_5fframe_2eproto() {
    protobuf_AddDesc_QDP_5fmain_5fframe_2eproto();
  }
} static_descriptor_initializer_QDP_5fmain_5fframe_2eproto_;
const ::google::protobuf::EnumDescriptor* other_platform_descriptor() {
  protobuf_AssignDescriptorsOnce();
  return other_platform_descriptor_;
}
bool other_platform_IsValid(int value) {
  switch(value) {
    case 0:
    case 1:
    case 2:
    case 3:
      return true;
    default:
      return false;
  }
}


// ===================================================================

#ifndef _MSC_VER
const int user_verification_ask::kInfoFieldNumber;
const int user_verification_ask::kPlatformTypeFieldNumber;
const int user_verification_ask::kAskHeaderFieldNumber;
const int user_verification_ask::kServiceManagerFieldNumber;
const int user_verification_ask::kQueryTypeFieldNumber;
#endif  // !_MSC_VER

user_verification_ask::user_verification_ask()
  : ::google::protobuf::Message() {
  SharedCtor();
  // @@protoc_insertion_point(constructor:QDP_main_frame.user_verification_ask)
}

void user_verification_ask::InitAsDefaultInstance() {
  info_ = const_cast< ::QDP_basic_info::user_basic_info*>(&::QDP_basic_info::user_basic_info::default_instance());
  ask_header_ = const_cast< ::common::common_ask_header*>(&::common::common_ask_header::default_instance());
  service_manager_ = const_cast< ::QDP_basic_info::control_service*>(&::QDP_basic_info::control_service::default_instance());
}

user_verification_ask::user_verification_ask(const user_verification_ask& from)
  : ::google::protobuf::Message() {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:QDP_main_frame.user_verification_ask)
}

void user_verification_ask::SharedCtor() {
  _cached_size_ = 0;
  info_ = NULL;
  platform_type_ = 0;
  ask_header_ = NULL;
  service_manager_ = NULL;
  query_type_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

user_verification_ask::~user_verification_ask() {
  // @@protoc_insertion_point(destructor:QDP_main_frame.user_verification_ask)
  SharedDtor();
}

void user_verification_ask::SharedDtor() {
  if (this != default_instance_) {
    delete info_;
    delete ask_header_;
    delete service_manager_;
  }
}

void user_verification_ask::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* user_verification_ask::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return user_verification_ask_descriptor_;
}

const user_verification_ask& user_verification_ask::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_QDP_5fmain_5fframe_2eproto();
  return *default_instance_;
}

user_verification_ask* user_verification_ask::default_instance_ = NULL;

user_verification_ask* user_verification_ask::New() const {
  return new user_verification_ask;
}

void user_verification_ask::Clear() {
#define OFFSET_OF_FIELD_(f) (reinterpret_cast<char*>(      \
  &reinterpret_cast<user_verification_ask*>(16)->f) - \
   reinterpret_cast<char*>(16))

#define ZR_(first, last) do {                              \
    size_t f = OFFSET_OF_FIELD_(first);                    \
    size_t n = OFFSET_OF_FIELD_(last) - f + sizeof(last);  \
    ::memset(&first, 0, n);                                \
  } while (0)

  if (_has_bits_[0 / 32] & 31) {
    ZR_(platform_type_, query_type_);
    if (has_info()) {
      if (info_ != NULL) info_->::QDP_basic_info::user_basic_info::Clear();
    }
    if (has_ask_header()) {
      if (ask_header_ != NULL) ask_header_->::common::common_ask_header::Clear();
    }
    if (has_service_manager()) {
      if (service_manager_ != NULL) service_manager_->::QDP_basic_info::control_service::Clear();
    }
  }

#undef OFFSET_OF_FIELD_
#undef ZR_

  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  mutable_unknown_fields()->Clear();
}

bool user_verification_ask::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:QDP_main_frame.user_verification_ask)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional .QDP_basic_info.user_basic_info info = 1;
      case 1: {
        if (tag == 10) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_info()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(16)) goto parse_platform_type;
        break;
      }

      // optional .QDP_main_frame.other_platform platform_type = 2;
      case 2: {
        if (tag == 16) {
         parse_platform_type:
          int value;
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   int, ::google::protobuf::internal::WireFormatLite::TYPE_ENUM>(
                 input, &value)));
          if (::QDP_main_frame::other_platform_IsValid(value)) {
            set_platform_type(static_cast< ::QDP_main_frame::other_platform >(value));
          } else {
            mutable_unknown_fields()->AddVarint(2, value);
          }
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(26)) goto parse_ask_header;
        break;
      }

      // optional .common.common_ask_header ask_header = 3;
      case 3: {
        if (tag == 26) {
         parse_ask_header:
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_ask_header()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(34)) goto parse_service_manager;
        break;
      }

      // optional .QDP_basic_info.control_service service_manager = 4;
      case 4: {
        if (tag == 34) {
         parse_service_manager:
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_service_manager()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(40)) goto parse_query_type;
        break;
      }

      // optional int32 query_type = 5 [default = 0];
      case 5: {
        if (tag == 40) {
         parse_query_type:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &query_type_)));
          set_has_query_type();
        } else {
          goto handle_unusual;
        }
        if (input->ExpectAtEnd()) goto success;
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0 ||
            ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:QDP_main_frame.user_verification_ask)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:QDP_main_frame.user_verification_ask)
  return false;
#undef DO_
}

void user_verification_ask::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:QDP_main_frame.user_verification_ask)
  // optional .QDP_basic_info.user_basic_info info = 1;
  if (has_info()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      1, this->info(), output);
  }

  // optional .QDP_main_frame.other_platform platform_type = 2;
  if (has_platform_type()) {
    ::google::protobuf::internal::WireFormatLite::WriteEnum(
      2, this->platform_type(), output);
  }

  // optional .common.common_ask_header ask_header = 3;
  if (has_ask_header()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      3, this->ask_header(), output);
  }

  // optional .QDP_basic_info.control_service service_manager = 4;
  if (has_service_manager()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      4, this->service_manager(), output);
  }

  // optional int32 query_type = 5 [default = 0];
  if (has_query_type()) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(5, this->query_type(), output);
  }

  if (!unknown_fields().empty()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:QDP_main_frame.user_verification_ask)
}

::google::protobuf::uint8* user_verification_ask::SerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:QDP_main_frame.user_verification_ask)
  // optional .QDP_basic_info.user_basic_info info = 1;
  if (has_info()) {
    target = ::google::protobuf::internal::WireFormatLite::
      WriteMessageNoVirtualToArray(
        1, this->info(), target);
  }

  // optional .QDP_main_frame.other_platform platform_type = 2;
  if (has_platform_type()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteEnumToArray(
      2, this->platform_type(), target);
  }

  // optional .common.common_ask_header ask_header = 3;
  if (has_ask_header()) {
    target = ::google::protobuf::internal::WireFormatLite::
      WriteMessageNoVirtualToArray(
        3, this->ask_header(), target);
  }

  // optional .QDP_basic_info.control_service service_manager = 4;
  if (has_service_manager()) {
    target = ::google::protobuf::internal::WireFormatLite::
      WriteMessageNoVirtualToArray(
        4, this->service_manager(), target);
  }

  // optional int32 query_type = 5 [default = 0];
  if (has_query_type()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(5, this->query_type(), target);
  }

  if (!unknown_fields().empty()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:QDP_main_frame.user_verification_ask)
  return target;
}

int user_verification_ask::ByteSize() const {
  int total_size = 0;

  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    // optional .QDP_basic_info.user_basic_info info = 1;
    if (has_info()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
          this->info());
    }

    // optional .QDP_main_frame.other_platform platform_type = 2;
    if (has_platform_type()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::EnumSize(this->platform_type());
    }

    // optional .common.common_ask_header ask_header = 3;
    if (has_ask_header()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
          this->ask_header());
    }

    // optional .QDP_basic_info.control_service service_manager = 4;
    if (has_service_manager()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
          this->service_manager());
    }

    // optional int32 query_type = 5 [default = 0];
    if (has_query_type()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::Int32Size(
          this->query_type());
    }

  }
  if (!unknown_fields().empty()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void user_verification_ask::MergeFrom(const ::google::protobuf::Message& from) {
  GOOGLE_CHECK_NE(&from, this);
  const user_verification_ask* source =
    ::google::protobuf::internal::dynamic_cast_if_available<const user_verification_ask*>(
      &from);
  if (source == NULL) {
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
    MergeFrom(*source);
  }
}

void user_verification_ask::MergeFrom(const user_verification_ask& from) {
  GOOGLE_CHECK_NE(&from, this);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_info()) {
      mutable_info()->::QDP_basic_info::user_basic_info::MergeFrom(from.info());
    }
    if (from.has_platform_type()) {
      set_platform_type(from.platform_type());
    }
    if (from.has_ask_header()) {
      mutable_ask_header()->::common::common_ask_header::MergeFrom(from.ask_header());
    }
    if (from.has_service_manager()) {
      mutable_service_manager()->::QDP_basic_info::control_service::MergeFrom(from.service_manager());
    }
    if (from.has_query_type()) {
      set_query_type(from.query_type());
    }
  }
  mutable_unknown_fields()->MergeFrom(from.unknown_fields());
}

void user_verification_ask::CopyFrom(const ::google::protobuf::Message& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void user_verification_ask::CopyFrom(const user_verification_ask& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool user_verification_ask::IsInitialized() const {

  return true;
}

void user_verification_ask::Swap(user_verification_ask* other) {
  if (other != this) {
    std::swap(info_, other->info_);
    std::swap(platform_type_, other->platform_type_);
    std::swap(ask_header_, other->ask_header_);
    std::swap(service_manager_, other->service_manager_);
    std::swap(query_type_, other->query_type_);
    std::swap(_has_bits_[0], other->_has_bits_[0]);
    _unknown_fields_.Swap(&other->_unknown_fields_);
    std::swap(_cached_size_, other->_cached_size_);
  }
}

::google::protobuf::Metadata user_verification_ask::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = user_verification_ask_descriptor_;
  metadata.reflection = user_verification_ask_reflection_;
  return metadata;
}


// ===================================================================

#ifndef _MSC_VER
const int user_verification_ans::kPlatformTypeFieldNumber;
const int user_verification_ans::kJsonAnsFieldNumber;
const int user_verification_ans::kErrorFieldNumber;
#endif  // !_MSC_VER

user_verification_ans::user_verification_ans()
  : ::google::protobuf::Message() {
  SharedCtor();
  // @@protoc_insertion_point(constructor:QDP_main_frame.user_verification_ans)
}

void user_verification_ans::InitAsDefaultInstance() {
  error_ = const_cast< ::common::errorinfo*>(&::common::errorinfo::default_instance());
}

user_verification_ans::user_verification_ans(const user_verification_ans& from)
  : ::google::protobuf::Message() {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:QDP_main_frame.user_verification_ans)
}

void user_verification_ans::SharedCtor() {
  ::google::protobuf::internal::GetEmptyString();
  _cached_size_ = 0;
  platform_type_ = 0;
  json_ans_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  error_ = NULL;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

user_verification_ans::~user_verification_ans() {
  // @@protoc_insertion_point(destructor:QDP_main_frame.user_verification_ans)
  SharedDtor();
}

void user_verification_ans::SharedDtor() {
  if (json_ans_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    delete json_ans_;
  }
  if (this != default_instance_) {
    delete error_;
  }
}

void user_verification_ans::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* user_verification_ans::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return user_verification_ans_descriptor_;
}

const user_verification_ans& user_verification_ans::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_QDP_5fmain_5fframe_2eproto();
  return *default_instance_;
}

user_verification_ans* user_verification_ans::default_instance_ = NULL;

user_verification_ans* user_verification_ans::New() const {
  return new user_verification_ans;
}

void user_verification_ans::Clear() {
  if (_has_bits_[0 / 32] & 7) {
    platform_type_ = 0;
    if (has_json_ans()) {
      if (json_ans_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
        json_ans_->clear();
      }
    }
    if (has_error()) {
      if (error_ != NULL) error_->::common::errorinfo::Clear();
    }
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  mutable_unknown_fields()->Clear();
}

bool user_verification_ans::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:QDP_main_frame.user_verification_ans)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional .QDP_main_frame.other_platform platform_type = 1;
      case 1: {
        if (tag == 8) {
          int value;
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   int, ::google::protobuf::internal::WireFormatLite::TYPE_ENUM>(
                 input, &value)));
          if (::QDP_main_frame::other_platform_IsValid(value)) {
            set_platform_type(static_cast< ::QDP_main_frame::other_platform >(value));
          } else {
            mutable_unknown_fields()->AddVarint(1, value);
          }
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(18)) goto parse_json_ans;
        break;
      }

      // optional bytes json_ans = 2;
      case 2: {
        if (tag == 18) {
         parse_json_ans:
          DO_(::google::protobuf::internal::WireFormatLite::ReadBytes(
                input, this->mutable_json_ans()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(26)) goto parse_error;
        break;
      }

      // optional .common.errorinfo error = 3;
      case 3: {
        if (tag == 26) {
         parse_error:
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_error()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectAtEnd()) goto success;
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0 ||
            ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:QDP_main_frame.user_verification_ans)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:QDP_main_frame.user_verification_ans)
  return false;
#undef DO_
}

void user_verification_ans::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:QDP_main_frame.user_verification_ans)
  // optional .QDP_main_frame.other_platform platform_type = 1;
  if (has_platform_type()) {
    ::google::protobuf::internal::WireFormatLite::WriteEnum(
      1, this->platform_type(), output);
  }

  // optional bytes json_ans = 2;
  if (has_json_ans()) {
    ::google::protobuf::internal::WireFormatLite::WriteBytesMaybeAliased(
      2, this->json_ans(), output);
  }

  // optional .common.errorinfo error = 3;
  if (has_error()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      3, this->error(), output);
  }

  if (!unknown_fields().empty()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:QDP_main_frame.user_verification_ans)
}

::google::protobuf::uint8* user_verification_ans::SerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:QDP_main_frame.user_verification_ans)
  // optional .QDP_main_frame.other_platform platform_type = 1;
  if (has_platform_type()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteEnumToArray(
      1, this->platform_type(), target);
  }

  // optional bytes json_ans = 2;
  if (has_json_ans()) {
    target =
      ::google::protobuf::internal::WireFormatLite::WriteBytesToArray(
        2, this->json_ans(), target);
  }

  // optional .common.errorinfo error = 3;
  if (has_error()) {
    target = ::google::protobuf::internal::WireFormatLite::
      WriteMessageNoVirtualToArray(
        3, this->error(), target);
  }

  if (!unknown_fields().empty()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:QDP_main_frame.user_verification_ans)
  return target;
}

int user_verification_ans::ByteSize() const {
  int total_size = 0;

  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    // optional .QDP_main_frame.other_platform platform_type = 1;
    if (has_platform_type()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::EnumSize(this->platform_type());
    }

    // optional bytes json_ans = 2;
    if (has_json_ans()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::BytesSize(
          this->json_ans());
    }

    // optional .common.errorinfo error = 3;
    if (has_error()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
          this->error());
    }

  }
  if (!unknown_fields().empty()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void user_verification_ans::MergeFrom(const ::google::protobuf::Message& from) {
  GOOGLE_CHECK_NE(&from, this);
  const user_verification_ans* source =
    ::google::protobuf::internal::dynamic_cast_if_available<const user_verification_ans*>(
      &from);
  if (source == NULL) {
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
    MergeFrom(*source);
  }
}

void user_verification_ans::MergeFrom(const user_verification_ans& from) {
  GOOGLE_CHECK_NE(&from, this);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_platform_type()) {
      set_platform_type(from.platform_type());
    }
    if (from.has_json_ans()) {
      set_json_ans(from.json_ans());
    }
    if (from.has_error()) {
      mutable_error()->::common::errorinfo::MergeFrom(from.error());
    }
  }
  mutable_unknown_fields()->MergeFrom(from.unknown_fields());
}

void user_verification_ans::CopyFrom(const ::google::protobuf::Message& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void user_verification_ans::CopyFrom(const user_verification_ans& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool user_verification_ans::IsInitialized() const {

  return true;
}

void user_verification_ans::Swap(user_verification_ans* other) {
  if (other != this) {
    std::swap(platform_type_, other->platform_type_);
    std::swap(json_ans_, other->json_ans_);
    std::swap(error_, other->error_);
    std::swap(_has_bits_[0], other->_has_bits_[0]);
    _unknown_fields_.Swap(&other->_unknown_fields_);
    std::swap(_cached_size_, other->_cached_size_);
  }
}

::google::protobuf::Metadata user_verification_ans::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = user_verification_ans_descriptor_;
  metadata.reflection = user_verification_ans_reflection_;
  return metadata;
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace QDP_main_frame

// @@protoc_insertion_point(global_scope)
